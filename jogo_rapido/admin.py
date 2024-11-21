from django.contrib import admin
from .models import QuadraGeral

class QuadraGeralAdmin (admin.ModelAdmin):
  list_display = ['imagem','esporte', 'localizacao', 'qualidade']


admin.site.register(QuadraGeral, QuadraGeralAdmin)