from django.urls import path

from gestaoacoes.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('acesso_nao_permitido/', views.acesso_nao_permitido, name='acesso_nao_permitido'),

]