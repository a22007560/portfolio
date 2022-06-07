from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Blog, PontuacaoQuizz
from .forms import BlogForm

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')


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
    return render(request, 'portfolio/login.html')

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
