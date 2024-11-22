# Generated by Django 5.0.2 on 2024-11-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jogo_rapido", "0002_quadrageral_delete_quadra"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("futebol", "Futebol"),
                            ("basquete", "Basquete"),
                            ("volei", "Vôlei"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
