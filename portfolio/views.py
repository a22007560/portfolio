from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import Blog, Project, PontuacaoQuizz, Cadeira, TFC
from .forms import BlogForm, ProjectForm, CadeiraForm, TFCForm

import base64
import datetime
import io
import urllib

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)

def novaCadeira_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    form = CadeiraForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form}

    return render(request, 'portfolio/novaCadeira.html', context)

def edita_cadeira_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editCadeira.html', context)


def apaga_cadeira_view(request, cadeira_id):
    Cadeira.objects.get(id=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))

def projetos_page_view(request):
    context = {'projetos': Project.objects.all(),
               'tfcs': TFC.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def newProject_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    form = ProjectForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/newProject.html', context)

def newTFC_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    form = TFCForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/newTFC.html', context)

def edita_tfc_view(request, tfc_id):
    tfc = TFC.objects.get(id=tfc_id)
    form = ProjectForm(request.POST or None, instance=tfc)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'tfc_id': tfc_id}
    return render(request, 'portfolio/editTFC.html', context)

def apaga_tfc_view(request, tfc_id):
    TFC.objects.get(id=tfc_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

def edita_project_view(request, project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'project_id': project_id}
    return render(request, 'portfolio/editProjecto.html', context)


def apaga_project_view(request, project_id):
    Project.objects.get(id=project_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))


def blog_page_view(request):
    context = {'posts': Blog.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def nova_blog_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/newPost.html', context)


def edita_blog_view(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    form = BlogForm(request.POST or None, instance=blog)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'blog_id': blog_id}
    return render(request, 'portfolio/editPost.html', context)


def apaga_blog_view(request, blog_id):
    Blog.objects.get(id=blog_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def quizz_page_view(request):
    if request.method == 'POST':
        pontuacao = pontuacao_quizz(request)
        name = request.POST['nome']
        resultado = PontuacaoQuizz(nome=name, pontuacao=pontuacao)
        resultado.save()

    context = {
        'data': desenha_grafico_resultados(request),
    }

    return render(request, 'portfolio/quizz.html', context)


def login_page_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')

def logout_page_view(request):
    logout(request)

    return render(request, 'portfolio/home.html', {
                'message': 'Foi desconetado.'
            })

def weather_page_view(request):
    return render(request, 'portfolio/weather.html')

def factos_page_view(request):
    return render(request, 'portfolio/factos.html')

def noticias_page_view(request):
    return render(request, 'portfolio/noticias.html')

def pontuacao_quizz(request):
    score = 0
    lista_checkBox = request.POST.getlist('op21')

    if request.POST['pergunta1'] == 'op2':
        score += 1

    if 'op21' in lista_checkBox:
        score += 1

    if 'op23' in lista_checkBox:
        score += 1

    if 'op22' in lista_checkBox:
        if score > 0:
            score -= 1

    if request.POST['op31'] == 'Hypertext Markup Language' or request.POST['op31'] == 'hypertext markup language':
        score += 1

    if request.POST['op41'] == '1991':
        score += 1

    return score

def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all().order_by('pontuacao')
    lista_nomes = []
    lista_pontuacao = []

    for person in pontuacoes:
        lista_nomes.append(person.nome)
        lista_pontuacao.append(person.pontuacao)

    plt.barh(lista_nomes, lista_pontuacao)
    plt.ylabel("Nomes")
    plt.xlabel("Pontuação")
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')

    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri