from django.urls import path

from gestaoacoes.base.apps.movimentacoes import views

app_name = 'movimentacoes'

urlpatterns = [
    path('', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('nova-movimentacao', views.nova_movimentacao, name='nova_movimentacao'),
    ]