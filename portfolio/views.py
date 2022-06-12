from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import Blog, Project, PontuacaoQuizz, Cadeira
from .forms import BlogForm, ProjectForm, CadeiraForm

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
    context = {'projetos': Project.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def newProject_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    form = ProjectForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/newProject.html', context)

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
    return render(request, 'portfolio/quizz.html')


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

def pontuacao_quizz(request):
    score = 0
    lista_checkBox = request.POST.getList('op21')

    if request.POST['pergunta1'] == 'teste':
        score += 1

    if 'respostaCerta' in lista_checkBox:
        score += 1

    if 'respostaErrada' in lista_checkBox:
        if score > 0:
            score -= 1

    return score


def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()

    desenha_grafico_resultados(request)
    return render(request, 'portfolio/quizz.html')


def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda objeto: objeto.pontuacao, reverse=False)
    listaNomes = []
    listapontuacao = []

    for person in pontuacao_sorted:
        listaNomes.append(person.nome)
        listapontuacao.append(person.pontuacao)

    plt.barh(listaNomes, listapontuacao)
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')
