from django.urls import path

from gestaoacoes.base.apps.configuracoes import views

app_name = 'configuracoes'
urlpatterns = [
    path('corretoras', views.lista_corretoras, name='lista_corretoras'),
    path('nova_corretora', views.nova_corretora, name='nova_corretora'),
    path('editar_corretora/<int:pk>/', views.editar_corretora.as_view(), name='editar_corretora'),
    path('deletar_corretora/<int:pk>/', views.deletar_corretora.as_view(), name='deletar_corretora'),

]