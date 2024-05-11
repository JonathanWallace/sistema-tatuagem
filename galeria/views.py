from django.shortcuts import render, redirect
from galeria.models import Arte, Tatuagem
from galeria.forms import EstiloForms, ColorizacaoForms, TamanhoForms, PromocaoForms, ArteForms, TatuagemForms

# Create your views here.

def home(request):
    artes = Arte.objects.all()
    tatuagens = Tatuagem.objects.all()
    data = {'cards_arte':artes, 'cards_tatu':tatuagens}
    return render(request, 'home.html', data)

def contato(request):
    return render(request, 'contato.html')

def catalogo(request):
    artes = Arte.objects.all()
    data = {'cards':artes}
    return render(request, 'catalogo.html', data)

def portfolio(request):
    tatus = Tatuagem.objects.all()
    data = {'cards':tatus}
    return render(request, 'portfolio.html', data)


def cadastro_estilo(request):
    form = EstiloForms()

    data = {
        'cad_url':'cad-estilo',
        'form':form,
        'cad_nome':'Novo Estilo'
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
        'cad_nome':'Novo Tamanho'
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
        'cad_nome':'Nova Colorização'
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
        'cad_nome':'Nova Promoção'
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
        'cad_nome':'Nova Arte'
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
        'cad_nome':'Nova Tatuagem'
        }

    if request.method == 'POST':
        form = TatuagemForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', data)


