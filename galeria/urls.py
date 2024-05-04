from django.urls import path
from galeria.views import home, cadastro_estilo, cadastro_tamanho, cadastro_color, cadastro_promo, cadastro_arte, cadastro_tatuagem

urlpatterns = [
    path('', home, name='home'),
    path('cadastro_promo', cadastro_promo, name='cad-promo'),
    path('cadastro_estilo', cadastro_estilo, name='cad-estilo'),
    path('cadastro_tamanho', cadastro_tamanho, name='cad-tamanho'),
    path('cadastro_color', cadastro_color, name='cad-color'),
    path('cadastro_arte', cadastro_arte, name='cad-arte'),
    path('cadastro_tatuagem', cadastro_tatuagem, name='cad-tatuagem'),
   
]