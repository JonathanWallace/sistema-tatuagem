from django.shortcuts import render, redirect, get_object_or_404
from galeria.models import Arte, Tatuagem
from galeria.forms import EstiloForms, ColorizacaoForms, TamanhoForms, PromocaoForms, ArteForms, TatuagemForms, LoginForms
from django.contrib import auth, messages


def validador(func):
    def verificar(*args, **kwargs):
        if not args[0].user.is_authenticated:
            messages.error(args[0], f'Você precisa estar logado!')
            return redirect('login')
        else:
            return func(*args,**kwargs)
    return verificar

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

def detail_arte(request, arte_id):
    arte = get_object_or_404(Arte, pk=arte_id)
    return render(request, 'arte_detail.html', {'arte':arte})

def portfolio(request):
    tatus = Tatuagem.objects.all()
    data = {'cards':tatus}
    return render(request, 'portfolio.html', data)

@validador
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

@validador
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

@validador
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

@validador
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

@validador
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

@validador
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

@validador
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('home')


def logar(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request, username=nome, password=senha)
        
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, f'Erro ao logar')
            return redirect('login')


    return render(request, 'login.html', {'form':form})

@validador
def deletar(request, arte_id):
    arte = Arte.objects.get(id=arte_id)
    arte.delete()
    messages.success(request, f"Arte:{arte.arte_nome} excluida com sucesso!")
    return redirect('home')
