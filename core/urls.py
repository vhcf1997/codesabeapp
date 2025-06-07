from core import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),  # noqa E501
    path('cadastro/', views.cadastro, name='cadastro'),
    path('detalhe/<int:pk>/', views.detalhe, name='detalhe'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('notas/', views.lista_notas, name='lista_notas'),
    path('nota/<int:pk>/editar/', views.editar_nota, name='editar_nota'),
    path('nota/<int:pk>/excluir/', views.excluir_nota, name='excluir_nota'),
    path('linguagem/nova/', views.adicionar_linguagem, name='adicionar_linguagem'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),

]
