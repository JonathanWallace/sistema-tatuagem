from django.contrib import admin
from galeria.models import Arte, Tatuagem

class ListandoArtes(admin.ModelAdmin):
    list_display = ('id','arte_nome')
   
admin.site.register(Arte, ListandoArtes)

class ListandoTatuagens(admin.ModelAdmin):
    list_display = ('id','tatuagem_nome')
   
admin.site.register(Tatuagem, ListandoTatuagens)