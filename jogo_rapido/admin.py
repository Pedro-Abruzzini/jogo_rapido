from django.contrib import admin
from .models import QuadraGeral, Item

class QuadraGeralAdmin (admin.ModelAdmin):
  list_display = ['imagem','esporte', 'localizacao', 'qualidade']


admin.site.register(QuadraGeral, QuadraGeralAdmin)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
