from django.db import models

class QuadraGeral (models.Model):
  imagem = models.URLField(max_length=1000)
  esporte = models.CharField(max_length=50)
  localizacao = models.CharField(max_length=50)
  qualidade = models.CharField(max_length=50, choices={
 'MB': 'Muito boa',
 'B': 'Boa',
 'M': 'Mediana',
 'R': 'Ruim',
 'MR': 'Muito ruim'
  })
  
