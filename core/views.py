from django.shortcuts import render, redirect
from .forms import NotaForm
from django.utils.timezone import now
from .models import Linguagem, Nota


def index(request):
    ultimas_notas = Nota.objects.order_by('-dataEdicao')[:5]

    return render(request, 'index.html', {'ultimas_notas': ultimas_notas})

def cadastro(request):

    linguagens = Linguagem.objects.all()

    if request.method == 'POST':
        form = NotaForm(request.POST)

        if form.is_valid():
            form.save()
            print("Tipo", form.cleaned_data['tipo'])
            print("Nome", form.cleaned_data['nome'])
            return redirect('core:index')
        else:
            print("Formulário inválido:")
            print(form.errors)  # 🪵 LOG DE ERROS!
    else:
        form = NotaForm()


    # Este valor é uma prévia do que será salvo como dataCriacao
    data_criacao_preview = now()

    return render(request, 'cadastro.html', {
        'form': form,
        'data_criacao_preview': data_criacao_preview,
        'linguagens': linguagens,
    })

def detalhe(request, pk):
    detalhes = Nota.objects.get(id=pk)

    context = {
        'detalhe': detalhes,
    }

    return render(request, 'detalhe.html', context)

def pesquisa(request):
    return render(request, 'pesquisa.html')
