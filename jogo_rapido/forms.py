from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Comentario


class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    tipo_usuario = forms.ChoiceField(
        choices=[('USUARIO', 'Usuário de Quadras'), ('PROPRIETARIO', 'Proprietário de Quadras')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Tipo de Usuário",
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'tipo_usuario']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto', 'estrelas']
        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Digite seu comentário aqui...', 'rows': 4}),
            'estrelas': forms.Select()
        }