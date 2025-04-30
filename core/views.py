from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def detalhe(request):
    return render(request, 'detalhe.html')

def pesquisa(request):
    return render(request, 'pesquisa.html')

