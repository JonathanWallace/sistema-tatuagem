from django import forms
from galeria.models import Estilo, Colorizacao, Tamanho, Promocao, Arte, Tatuagem

class EstiloForms(forms.ModelForm):
    class Meta:
        model = Estilo

        exclude = []      

        labels = {
            'estilo_nome':'Estilo',
            'estilo_dificuldade': 'Dificuldade'
        }

        widgets = {
            'estilo_nome': forms.TextInput(attrs={"class":"form-control"}),
            'estilo_dificuldade': forms.Select(attrs={'class':"form-control"}),
        }

class ColorizacaoForms(forms.ModelForm):
    class Meta:
        model = Colorizacao   
        exclude = []      

        labels = {
            'colorizacao_nome':'Colorização',
        }

        widgets = {
            'colorizacao_nome': forms.TextInput(attrs={"class":"form-control"}),
        }

class TamanhoForms(forms.ModelForm):
    class Meta:
        model = Tamanho       
        exclude = [] 

        labels = {
            'tamanho_nome':'Nome',
            'tamanho_dimensao': 'Centímetros'
        }

        widgets = {
            'tamanho_nome': forms.TextInput(attrs={"class":"form-control"}),
            'tamanho_dimensao': forms.TextInput(attrs={'class':"form-control"}),
        }

class PromocaoForms(forms.ModelForm):
    class Meta:
        model = Promocao       
        exclude = []  

        labels = {
            'promo_nome':'Nome',
            'promo_data_inicio': 'Inicio',
            'promo_data_fim': 'Termino',
            'promo_ativa':'Ativa',
        }

        widgets = {
            'promo_nome': forms.TextInput(attrs={"class":"form-control"}),
            'promo_data_inicio': forms.DateInput(attrs={'class':"form-control"}),
            'promo_data_fim': forms.DateInput(attrs={'class':"form-control"}),
            'promo_ativa': forms.CheckboxInput(),

        }

class ArteForms(forms.ModelForm):
    class Meta:
        model = Arte        
        exclude = [] 

        labels = {
            'arte_nome':'Nome',
            'arte_estilo': 'Estilo',
            'arte_colorizacao': 'Colorização',
            'arte_preco':'Preço',
            'arte_qntd_sessoes': 'Quantidade de Sessões',
            'arte_promocao':'Promoção',
            'arte_wishlist':'Wishlist',
            'arte_imagem': 'Imagem',
        }

        widgets = {
            'arte_nome': forms.TextInput(attrs={"class":"form-control"}),
            'arte_estilo': forms.Select(attrs={'class':"form-control"}),
            'arte_colorizacao': forms.Select(attrs={'class':"form-control"}),
            'arte_preco': forms.TextInput(),
            'arte_qndt_sessoes': forms.TextInput(),
            'arte_promocao': forms.Select(),
            'arte_wishlist': forms.CheckboxInput(),
            'arte_imagem': forms.FileInput(attrs={'class':"form-control"}),

        }

class TatuagemForms(forms.ModelForm):
    class Meta:
        model = Tatuagem      
        exclude = []  

        labels = {
            'tatuagem_nome':'Nome',
            'tatuagem_nome_cliente':'Cliente',
            'tatuagem_data':'Data',
            'tatuagem_estilo': 'Estilo',
            'tatuagem_colorizacao': 'Colorização',
            'tatuagem_tamanho': 'Tamanho',
            'tatuagem_lugar_corpo':'Parte do Corpo',
            'tatuagem_local_servico':'Local',
            'tatuagem_preco':'Preço',
            'tatuagem_duracao_servico': 'Tempo de Serviço',
            'tatuagem_imagem': 'Imagem',
        }

        widgets = {
            'tatuagem_nome': forms.TextInput(attrs={"class":"form-control"}),
            'tatuagem_nome_cliente': forms.TextInput(attrs={"class":"form-control"}),
            'tatuagem_data': forms.DateInput(attrs={"class":"form-control"}),
            'tatuagem_estilo': forms.Select(attrs={'class':"form-control"}),
            'tatuagem_colorizacao': forms.Select(attrs={'class':"form-control"}),
            'tatuagem_tamanho': forms.Select(attrs={'class':"form-control"}),
            'tatuagem_lugar_corpo': forms.TextInput(attrs={"class":"form-control"}),
            'tatuagem_local_servico': forms.TextInput(attrs={"class":"form-control"}),
            'tatuagem_preco': forms.TextInput(),
            'tatuagem_duracao_servico': forms.TextInput(),
            'tatuagem_imagem': forms.FileInput(attrs={'class':"form-control"}),

        }
