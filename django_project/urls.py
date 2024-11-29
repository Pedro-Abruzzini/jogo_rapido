"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from jogo_rapido import views


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('login/', views.login_usuario),
    path('cadastro_usuario/',views.cadastro_usuario),
    path('filtro_items/', views.filter_items, name='filter_items'),  # Página principal com filtro
    path('add-to-favorites/<int:item_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('quadra/<int:quadra_id>/', views.detalhes_quadra, name='detalhes_quadra'),
    path('quadra/<int:quadra_id>/adicionar_comentario/', views.adicionar_comentario, name='adicionar_comentario'),
    path('quadra/<int:quadra_id>/horarios_disponiveis/', views.horarios_disponiveis, name='horarios_disponiveis'),
    path('quadra/<int:quadra_id>/reservar/', views.reservar_horario, name='reservar_horario'),
]


