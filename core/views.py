from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import NotaForm, LinguagemForm
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
    notas = Nota.objects.all().order_by('-dataEdicao')
    linguagens = Linguagem.objects.all()

    query = request.GET.get('q', '')
    tipos = request.GET.getlist('tipo')
    linguagem_id = request.GET.get('linguagem', '')

    if query:
        notas = notas.filter(
            Q(nome__icontains=query)
            | Q(descricao__icontains=query)
            | Q(exemplo__icontains=query)
            | Q(palavraChave__icontains=query)
        )

    if tipos:
        notas = notas.filter(tipo__in=tipos)

    if linguagem_id:
        notas = notas.filter(linguagem_id=linguagem_id)

    context = {
        'notas': notas,
        'linguagens': linguagens,
        'query': query,
        'tipos': tipos,
        'linguagem_id': linguagem_id,
    }

    return render(request, 'pesquisa.html', context)


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


def adicionar_linguagem(request):
    if request.method == 'POST':
        form = LinguagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:cadastro')
    else:
        form = LinguagemForm()

    return render(request, 'adicionar_linguagem.html', {'form': form})
