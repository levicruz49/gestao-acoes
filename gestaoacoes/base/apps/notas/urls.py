from django.urls import path

from gestaoacoes.base.apps.notas import views

app_name = 'notas'
urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('nova-nota', views.nova_nota, name='nova_nota'),
    path('novo-ativo-nota/<int:fk_nota>/', views.novo_ativo_nota, name="novo_ativo_nota"),
    path('nova-taxa-nota/<int:fk_nota>/', views.novo_taxa_nota, name="novo_taxa_nota"),
    path('incluir-ativo-nova/<int:fk_nota>/', views.incluir_ativo_nova, name="incluir_ativo_nova"),
]
