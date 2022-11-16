from django.urls import path

from gestaoacoes.base.apps.notas import views

app_name = 'notas'
urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('nova-nota', views.nova_nota, name='nova_nota'),
    path('novo-ativo-nota/<int:fk_nota>/', views.novo_ativo_nota, name="novo_ativo_nota"),
    path('incluir-ativo-nota/<int:fk_nota>/', views.incluir_ativo_nota, name="incluir_ativo_nota"),
    path('nova-taxa-nota/<int:fk_nota>/', views.nova_taxa_nota, name="nova_taxa_nota"),
    path('editar-nota/<int:fk_nota>/', views.editar_nota.as_view(), name="editar_nota"),
    path('editar-ativo/<int:fk_nota>/', views.editar_ativo.as_view(), name="editar_ativo"),
    path('detalhes-nota/<int:fk_nota>/', views.detalhes_nota, name="detalhes_nota"),
    path('deletar-nota/<int:fk_nota>/', views.deletar_nota.as_view(), name="deletar_nota"),
    path('deletar-ativo-detalhes/<int:fk_nota>/', views.deletar_ativo_detalhes.as_view(), name="deletar_ativo_detalhes"),
    path('deletar-ativo-incluir/<int:fk_nota>/', views.deletar_ativo_incluir.as_view(), name="deletar_ativo_incluir"),

    # path('incluir-ativo-nova/<int:fk_nota>/', views.incluir_ativo_nova, name="incluir_ativo_nova"),
    path('lista-splits-inplits', views.lista_split_inplit, name="lista_split_inplit"),
    path('split-inplit', views.novo_split_inplit, name="novo_split_inplit"),
]
