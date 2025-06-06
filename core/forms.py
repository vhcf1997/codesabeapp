from django import forms
from .models import Nota, Linguagem

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
