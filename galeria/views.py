from django.shortcuts import render, redirect
from galeria.models import Estilo
from galeria.forms import EstiloForms, ColorizacaoForms, TamanhoForms, PromocaoForms, ArteForms, TatuagemForms

# Create your views here.

def home(request):
    data = {'title':'Galeria'}
    return render(request, 'home.html', data)


def cadastro_estilo(request):
    form = EstiloForms()

    data = {
        'cad_url':'cad-estilo',
        'form':form,
        }

    if request.method == 'POST':
        form = EstiloForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', data)


def cadastro_tamanho(request):
    form = TamanhoForms()
    data = {
        'cad_url':'cad-tamanho',
        'form':form,
        }

    if request.method == 'POST':
        form = TamanhoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', data)


def cadastro_color(request):
    form= ColorizacaoForms()
    data = {
        'cad_url':'cad-color',
        'form':form,
        }

    if request.method == 'POST':
        form = ColorizacaoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', data)


def cadastro_promo(request):
    form = PromocaoForms()
    data = {
        'cad_url':'cad-promo',
        'form':form,
        }

    if request.method == 'POST':
        form = PromocaoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', data)

def cadastro_arte(request):
    form = ArteForms()
    data = {
        'cad_url':'cad-arte',
        'form':form,
        }

    if request.method == 'POST':
        form = ArteForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', data)

def cadastro_tatuagem(request):
    form = TatuagemForms()
    data = {
        'cad_url':'cad-tatuagem',
        'form':form,
        }

    if request.method == 'POST':
        form = TatuagemForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', data)


