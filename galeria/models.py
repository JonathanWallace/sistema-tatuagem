from django.db import models
from django.core.validators import MinValueValidator
import re
from datetime import datetime


class Estilo(models.Model):
    DIFICULDADES = ([('FÁCIL','Fácil'),('MÉDIA','Média'),('DIFÍCIL','Difícil')]) 

    estilo_nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    estilo_dificuldade = models.CharField(max_length=100, choices=DIFICULDADES, default='')    

    def __str__(self):
        return self.estilo_nome
    

class Colorizacao(models.Model):
    colorizacao_nome = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.colorizacao_nome


class Tamanho(models.Model):
    tamanho_nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    tamanho_min = models.IntegerField(null=False, blank=False)
    tamanho_max = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.tamanho_nome

class Promocao(models.Model):
    promo_nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    promo_data_inicio = models.DateField()
    promo_data_fim = models.DateTimeField()
    promo_ativa = models.BooleanField(default=False)

    def __str__(self):
        return self.promo_nome
    

class Arte(models.Model):

    def get_path(self, fp):
        nome = re.sub(r"\s+", "", str(self.arte_nome)),
        estilo = re.sub(r"\s+", "", str(self.arte_estilo))                      
        color = re.sub(r"\s+", "", str(self.arte_colorizacao))
        extensao = str(fp).split(".")[1]
        return f"artes/{estilo}/{color}/{nome}.{extensao}"

    arte_nome = models.CharField(max_length=100, null=False, blank=False)    
    arte_estilo = models.ForeignKey(to=Estilo, on_delete=models.SET_NULL, null=True, blank=False, related_name='estilo_arte')
    arte_colorizacao = models.ForeignKey(to=Colorizacao, on_delete=models.SET_NULL, null=True, blank=False, related_name='colorizacao_arte')
    arte_tamanho = models.ForeignKey(to=Tamanho, on_delete=models.SET_NULL, null=True, blank=False, related_name='tamanho_arte')
    arte_preco = models.FloatField(max_length=8.2, null=False, blank=False)
    arte_qntd_sessoes = models.IntegerField(null=True, blank=True, default=1)
    arte_lugar_corpo = models.CharField(max_length=100, null=True, blank=True)
    arte_promocao = models.ForeignKey(to=Promocao, on_delete=models.SET_NULL, null=True, blank=True, related_name='promo_arte')
    arte_wishlist = models.BooleanField(default=False)
    arte_reservado = models.BooleanField(default=False)
    arte_imagem = models.ImageField(upload_to=get_path, blank=True)    

    def __str__(self) -> str:
        return self.arte_nome
    

class Tatuagem(models.Model):
    def get_path(self, fp):
        nome = re.sub(r"\s+", "", str(self.tatuagem_estilo))
        color = re.sub(r"\s+", "", str(self.tatuagem_colorizacao)) 
        tamanho = re.sub(r"\s+", "", str(self.tatuagem_tamanho)) 
        return f"tatuagens/{nome}/{color}/{tamanho}/{fp}"

    tatuagem_nome = models.CharField(max_length=100, null=False, blank=False)
    tatuagem_nome_cliente = models.CharField(max_length=100, null=True, blank=True)
    tatuagem_data = models.DateTimeField(default=datetime.now, blank=False)
    tatuagem_estilo = models.ForeignKey(to=Estilo, on_delete=models.SET_NULL, null=True, blank=False, related_name='estilo_tatuagem')
    tatuagem_colorizacao = models.ForeignKey(to=Colorizacao, on_delete=models.SET_NULL, null=True, blank=False, related_name='colorizacao_tatuagem')
    tatuagem_tamanho = models.ForeignKey(to=Tamanho, on_delete=models.SET_NULL, null=True, blank=False, related_name='tamanho_tatuagem')
    tatuagem_lugar_corpo = models.CharField(max_length=100, null=True, blank=True)
    tatuagem_local_servico = models.CharField(max_length=100, null=True, blank=True)
    tatuagem_preco = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)], null=False, blank=False)
    tatuagem_duracao_servico = models.IntegerField(null=True, blank=True)
    tatuagem_imagem = models.ImageField(upload_to=get_path, blank=True)

    def __str__(self) -> str:
        return self.tatuagem_nome
