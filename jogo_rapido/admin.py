from django.contrib import admin
from .models import QuadraGeral, Item, Comentario

class QuadraGeralAdmin (admin.ModelAdmin):
  list_display = ['imagem','esporte', 'localizacao', 'qualidade']


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['quadra', 'autor', 'estrelas', 'data_criacao']

admin.site.register(QuadraGeral, QuadraGeralAdmin)
admin.site.register(Comentario, ComentarioAdmin)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
