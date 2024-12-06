# Generated by Django 5.1.3 on 2024-12-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jogo_rapido", "0007_perfilusuario_favoritos"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="perfilusuario",
            name="favoritos",
        ),
        migrations.AddField(
            model_name="perfilusuario",
            name="quadras_favoritas",
            field=models.ManyToManyField(
                blank=True,
                related_name="usuarios_favoritos",
                to="jogo_rapido.quadrageral",
            ),
        ),
    ]