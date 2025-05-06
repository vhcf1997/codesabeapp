from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),  # noqa E501
    path('cadastro/', views.cadastro, name='cadastro'),
    path('detalhe/<int:pk>/', views.detalhe, name='detalhe'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),

]
