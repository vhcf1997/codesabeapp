from django import forms
from .models import Nota, Linguagem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = [
            'tipo', 'nome', 'linguagem', 'descricao',
            'exemplo', 'palavraChave',
        ]
        widgets = {
            'descricao': forms.Textarea(
                attrs={
                    'rows': 4,
                    'class': 'form-control',
                    'placeholder': 'Descreva o item',
                }
            ),
            'exemplo': forms.Textarea(
                attrs={
                    'rows': 4,
                    'class': 'form-control code-editor',
                    'placeholder': 'Exemplo de código',
                }
            ),
            'palavraChave': forms.Textarea(
                attrs={
                    'rows': 2,
                    'class': 'form-control',
                    'placeholder': 'Palavras-chave',
                }
            ),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome do item'}
            ),
            'linguagem': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Linguagem'}
            ),
        }


class LinguagemForm(forms.ModelForm):
    class Meta:
        model = Linguagem
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

