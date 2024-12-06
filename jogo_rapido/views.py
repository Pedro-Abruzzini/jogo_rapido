from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import QuadraGeral, Item, Comentario, PerfilUsuario
from .forms import NovoUsuarioForm,ComentarioForm
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required





def cadastro_usuario(request):
    formulario = NovoUsuarioForm()
    if request.method == 'POST':
        formulario = NovoUsuarioForm(request.POST)
        if formulario.is_valid():
            novo_usuario = formulario.save()
            tipo_usuario = formulario.cleaned_data['tipo_usuario']
            PerfilUsuario.objects.create(usuario=novo_usuario, tipo_usuario=tipo_usuario)
            return redirect('/login')
    return render(request, 'cadastro_usuario.html', {'formulario': formulario})
  
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
    comentarios = Comentario.objects.select_related('quadra').order_by('-data_criacao')[:5]  # Apenas os 5 mais recentes
    return render(request, 'home.html', context={'quadrasgeral': quadrasgeral, 'comentarios': comentarios})

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


@login_required
def add_to_favorites(request, quadra_id):
    # Tenta encontrar a quadra pelo ID ou retorna um 404 se não existir
    quadra = get_object_or_404(QuadraGeral, id=quadra_id)

    # Adiciona ou remove a quadra dos favoritos do usuário logado
    if quadra in request.user.perfil.quadras_favoritas.all():
        request.user.perfil.quadras_favoritas.remove(quadra)
    else:
        request.user.perfil.quadras_favoritas.add(quadra)

    return JsonResponse({'status': 'success'})

def detalhes_quadra(request, quadra_id):
    try:
        quadra = QuadraGeral.objects.get(id=quadra_id)
    except QuadraGeral.DoesNotExist:
        return redirect('home')  # Redireciona para a home caso a quadra não exista

    media_estrelas = quadra.calcular_media_estrelas()
    return render(
        request,
        'detalhes_quadra.html',
        context={'quadra': quadra, 'media_estrelas': media_estrelas}
    )

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



def horarios_disponiveis(request, quadra_id):
    # Busca a quadra pelo ID ou retorna um erro 404
    quadra = get_object_or_404(QuadraGeral, id=quadra_id)
    horarios = quadra.horarios_disponiveis  # Já é uma lista no JSONField

    return render(request, 'horarios_disponiveis.html', {
        'quadra': quadra,
        'horarios': horarios  # Apenas passe a lista diretamente
    })

def reservar_horario(request, quadra_id):
    if request.method == 'POST':
        horario = request.POST.get('horario')
        # Processar a reserva do horário aqui
        return HttpResponse(f"Horário {horario} reservado com sucesso para a quadra {quadra_id}!")
    return redirect('horarios_disponiveis', quadra_id=quadra_id)

@login_required
def toggle_favorito(request, quadra_id):
    quadra = get_object_or_404(QuadraGeral, id=quadra_id)
    perfil = request.user.perfil
    if quadra in perfil.favoritos.all():
        perfil.favoritos.remove(quadra)
    else:
        perfil.favoritos.add(quadra)
    return redirect('detalhes_quadra', quadra_id=quadra.id)