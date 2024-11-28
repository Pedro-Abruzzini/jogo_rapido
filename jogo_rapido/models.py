from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

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

class Comentario(models.Model):
    quadra = models.ForeignKey(QuadraGeral, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  
    texto = models.TextField()
    estrelas = models.IntegerField(choices=[(i, f"{i} estrelas") for i in range(1, 6)])
    data_criacao = models.DateTimeField(default=now) 

    def __str__(self):
        return f"Comentário de {self.autor.username} - {self.quadra.localizacao} ({self.estrelas} estrelas)"