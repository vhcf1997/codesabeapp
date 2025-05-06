from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = [
            'tipo', 'nome', 'linguagem', 'descricao',
            'exemplo', 'palavraChave',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'exemplo': forms.Textarea(attrs={'rows': 4}),
            'palavraChave': forms.Textarea(attrs={'rows': 2}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'linguagem': forms.TextInput(attrs={'class': 'form-control'}),
        }