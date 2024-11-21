from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import QuadraGeral
from .forms import NovoUsuarioForm

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
