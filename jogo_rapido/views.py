from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import QuadraGeral, Item
from .forms import NovoUsuarioForm,ComentarioForm
from django.http import JsonResponse



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

def detalhes_quadra(request, quadra_id):
    try:
        quadra = QuadraGeral.objects.get(id=quadra_id)
    except QuadraGeral.DoesNotExist:
        return redirect('home')  # Redireciona para a página inicial se a quadra não existir
    return render(request, 'detalhes_quadra.html', context={'quadra': quadra})

def favoritos(request):
    favoritos_ids = request.session.get('favorites', [])
    favoritos = QuadraGeral.objects.filter(id__in=favoritos_ids)
    return render(request, 'favoritos.html', context={'favoritos': favoritos})

@login_required
def adicionar_comentario(request, quadra_id):
    try:
        quadra = QuadraGeral.objects.get(id=quadra_id)
    except QuadraGeral.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.quadra = quadra
            comentario.autor = request.user  # Associa o autor ao usuário logado
            comentario.save()
            return redirect('detalhes_quadra', quadra_id=quadra_id)
    else:
        form = ComentarioForm()

    return render(request, 'adicionar_comentario.html', {'form': form, 'quadra': quadra})