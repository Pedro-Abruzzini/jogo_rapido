from django.db import models

class QuadraGeral (models.Model):
  imagem = models.URLField(max_length=1000)
  esporte = models.CharField(max_length=50)
  localizacao = models.CharField(max_length=50)
  qualidade = models.CharField(
        max_length=50,
        choices=[
            ('MB', 'Muito boa'),
            ('B', 'Boa'),
            ('M', 'Mediana'),
            ('R', 'Ruim'),
            ('MR', 'Muito ruim')
        ]
    )

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('futebol', 'Futebol'),
        ('basquete', 'Basquete'),
        ('volei', 'Vôlei'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
