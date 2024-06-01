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

def dashboard_info():
    artes = Arte.objects.all()
    tatuagens = Tatuagem.objects.all()
    total_artes = len(artes)    
    valores = {
        'maior_valor':max([arte.arte_preco for arte in artes]), 
        'menor_valor': min([arte.arte_preco for arte in artes]),
        'media_valor':sum([arte.arte_preco for arte in artes])/len(artes)
        }
    count_estilos = {}
    count_tamanhos = {}
    count_wishlist = sum([1 for arte in artes if arte.arte_wishlist==True])
    for arte in artes:
        if arte.arte_estilo.estilo_nome not in count_estilos:
            count_estilos[arte.arte_estilo.estilo_nome] = 1
        else:
            count_estilos[arte.arte_estilo.estilo_nome] += 1
        if arte.arte_tamanho.tamanho_nome not in count_tamanhos:
            count_tamanhos[arte.arte_tamanho.tamanho_nome] = 1
        else:
            count_tamanhos[arte.arte_tamanho.tamanho_nome] += 1

    info = {'total_artes': total_artes,
            'count_estilos':count_estilos,
            'count_tamanhos':count_tamanhos,
            'valores':valores,
            'count_wishlist':count_wishlist}
    return info

def dashboard(request):
    data= {'infos':dashboard_info()}
    return render(request, 'dashboard.html', data)


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
    if request.user.is_authenticated:
        form = ArteForms(instance=arte)
        data = {
        'cad_url':'cad-arte',
        'arte':arte,
        'form':form,
        }        
        if request.method == 'POST':
            form = ArteForms(request.POST, request.FILES, instance=arte)
            if form.is_valid():
                form.save()
                data = {
                'cad_url':'cad-arte',
                'arte':arte,
                'form':form,
                }   
                return render(request, 'arte_detail.html', data)
        return render(request, 'arte_detail.html', data)
    else:
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
            return redirect('home')
        else:
            messages.error(request, f'Dados incorretos!')
            return redirect('login')


    return render(request, 'login.html', {'form':form})

@validador
def deletar(request, arte_id):
    try:
        arte = Arte.objects.get(id=arte_id)
        arte.delete()
    except Exception:
        pass
    return redirect('home')
