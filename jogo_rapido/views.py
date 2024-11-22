from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import QuadraGeral, Item
from .forms import NovoUsuarioForm
from django.http import JsonResponse


def inicio(request):
 return render(request, 'inicio.html')

def cadastro_usuario(request):
 formulario = NovoUsuarioForm()
 if request.method == 'POST' and request.POST:
  formulario = NovoUsuarioForm(request.POST)
  if formulario.is_valid():
    novo_usuario = formulario.save(commit=False)
    novo_usuario.email = formulario.cleaned_data['email']
    novo_usuario.first_name = formulario.cleaned_data['first_name']
    novo_usuario.last_name = formulario.cleaned_data['last_name']
    novo_usuario.save()
    return redirect('/login')
 return render(request, 'cadastro_usuario.html',
 {'formulario': formulario})
  
def login_usuario(request):
 formulario = AuthenticationForm()
 if request.method == 'POST' and request.POST:
    formulario = AuthenticationForm(request, request.POST)
    if formulario.is_valid():
        usuario = formulario.get_user()
        login(request, usuario)
        return redirect('/')
 return render(request, 'login.html', {'formulario': formulario}) 



def home(request):
    quadrasgeral = QuadraGeral.objects.all()
    return render(request, 'home.html', context= {'quadrasgeral': quadrasgeral})
        

def logout_usuario(request):
 logout(request)
 return redirect('/')


def filter_items(request):
    # Obtém o filtro selecionado
    filter_category = request.GET.get('filter', 'todos')
    if filter_category == 'todos':
        items = Item.objects.all()
    else:
        items = Item.objects.filter(category=filter_category)

    # Renderiza a página com os itens filtrados
    return render(request, 'filter_page.html', {'items': items, 'selected_filter': filter_category})


def add_to_favorites(request, item_id):
    # Simulação de favoritos (pode ser alterado para um modelo real de favoritos)
    item = Item.objects.get(id=item_id)
    request.session.setdefault('favorites', [])
    if item.name not in request.session['favorites']:
        request.session['favorites'].append(item.name)
        request.session.modified = True

    # Redireciona de volta para a página de filtro
    return redirect('filter_items')
