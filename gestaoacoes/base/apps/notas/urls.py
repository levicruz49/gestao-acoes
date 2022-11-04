from django.urls import path

from gestaoacoes.base.apps.notas import views

app_name = 'notas'
urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),

]
