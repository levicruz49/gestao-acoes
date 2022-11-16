from django.urls import path

from gestaoacoes.base.apps.configuracoes import views

app_name = 'resumos'
urlpatterns = [
    path('corretoras', views.lista_corretoras, name='lista_corretoras'),
    ]