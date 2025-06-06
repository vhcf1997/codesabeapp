from django.shortcuts import render, redirect, get_object_or_404
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


def lista_notas(request):
    notas = Nota.objects.all().order_by('-dataEdicao')
    return render(request, 'lista_notas.html', {'notas': notas})


def editar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    linguagens = Linguagem.objects.all()

    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('core:lista_notas')
    else:
        form = NotaForm(instance=nota)

    return render(request, 'editar_nota.html', {
        'form': form,
        'linguagens': linguagens,
    })


def excluir_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('core:lista_notas')
    return redirect('core:lista_notas')
