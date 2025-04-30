from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),  # noqa E501
    path('cadastro/', views.cadastro, name='cadastro'),
    path('detalhe/', views.detalhe, name='detalhe'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('editar/', views.editar, name='editar'),  # Para criação
    path('editar/<int:id>/', views.editar, name='editar'),  # Edição específica
    path('excluir/<int:id>/', views.excluir, name='excluir'),  # Nova view para exclusão
]
