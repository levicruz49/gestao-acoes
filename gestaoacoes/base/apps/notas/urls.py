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
    path('deletar-nota/<int:id_notas>/', views.deletar_nota, name="deletar_nota"),
    path('deletar-ativo-detalhes/<int:fk_nota>/', views.deletar_ativo_detalhes.as_view(), name="deletar_ativo_detalhes"),
    path('deletar-ativo-incluir/<int:fk_nota>/', views.deletar_ativo_incluir.as_view(), name="deletar_ativo_incluir"),

    # NOTAS DAYTRADE
    path('notas-daytrade', views.lista_notas_dt, name='lista_notas_dt'),
    path('nova-nota-daytrade', views.nova_nota_dt, name='nova_nota_dt'),
    path('novo-ativo-nota-dt/<int:fk_nota>/', views.novo_ativo_nota_dt, name="novo_ativo_nota_dt"),
    path('incluir-ativo-nota-dt/<int:fk_nota>/', views.incluir_ativo_nota_dt, name="incluir_ativo_nota_dt"),
    path('nova-taxa-nota-dt/<int:fk_nota>/', views.nova_taxa_nota_dt, name="nova_taxa_nota_dt"),
    path('editar-nota-dt/<int:fk_nota>/', views.editar_nota_dt.as_view(), name="editar_nota_dt"),
    path('editar-ativo-dt/<int:fk_nota>/', views.editar_ativo_dt.as_view(), name="editar_ativo_dt"),
    path('detalhes-nota-dt/<int:fk_nota_dt>/', views.detalhes_nota_dt, name="detalhes_nota_dt"),
    path('deletar-ativo-detalhes-dt/<int:fk_nota>/', views.deletar_ativo_detalhes_dt.as_view(), name="deletar_ativo_detalhes_dt"),
    path('deletar-ativo-incluir-dt/<int:fk_nota>/', views.deletar_ativo_incluir_dt.as_view(), name="deletar_ativo_incluir_dt"),

    # SPLIT INPLIT
    # path('incluir-ativo-nova/<int:fk_nota>/', views.incluir_ativo_nova, name="incluir_ativo_nova"),
    path('lista-splits-inplits', views.lista_split_inplit, name="lista_split_inplit"),
    path('split-inplit', views.novo_split_inplit, name="novo_split_inplit"),
]
