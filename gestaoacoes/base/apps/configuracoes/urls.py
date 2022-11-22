from django.urls import path

from gestaoacoes.base.apps.configuracoes import views

app_name = 'configuracoes'
urlpatterns = [
    path('corretoras', views.lista_corretoras, name='lista_corretoras'),
    path('nova_corretora', views.nova_corretora, name='nova_corretora'),
    path('editar_corretora/<int:pk>/', views.editar_corretora.as_view(), name='editar_corretora'),
    path('deletar_corretora/<int:pk>/', views.deletar_corretora.as_view(), name='deletar_corretora'),
    path('tipo_ativo', views.listar_tipos_ativo, name='listar_tipos_ativo'),
    path('novo_tipo_ativo', views.novo_tipo_ativo, name='novo_tipo_ativo'),
    path('editar_tipo_ativo/<int:pk>/', views.editar_tipo_ativo.as_view(), name='editar_tipo_ativo'),
    path('deletar_tipo_ativo/<int:pk>/', views.deletar_tipo_ativo.as_view(), name='deletar_tipo_ativo'),

]