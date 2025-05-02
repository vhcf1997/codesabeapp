from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Nota  # Supondo que você tenha um model Item

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def detalhe(request):
    return render(request, 'detalhe.html')

def pesquisa(request):
    return render(request, 'pesquisa.html')
