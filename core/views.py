from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item  # Supondo que você tenha um model Item

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def detalhe(request):
    return render(request, 'detalhe.html')

def pesquisa(request):
    return render(request, 'pesquisa.html')

def editar(request, id):
    item = get_object_or_404(Item, id=id)
    # Implemente a lógica de edição aqui
    return render(request, 'core/editar.html', {'item': item})

def excluir(request, id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=id)
        item.delete()
        return redirect('core:index')
    return redirect('core:detalhe', id=id)
