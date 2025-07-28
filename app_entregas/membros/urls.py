from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('entregas/',views.entregas, name='entregas'),
    path('membros/', views.membros, name='membros'),
    path('membros/excluir_membro/<slug:slug>/',views.excluir_membro,name='excluir_membro'),
    path('membros/adicionar_membro/',views.adicionar_membro, name='adicionar_membro'),
    path('membros/adicionar_membro/cadastrar_entregador/',views.cadastrar_entregador, name='cadastrar_entregador'),
    path('membros/editar_membro/<slug:slug>',views.editar_membro,name='editar_membro'),
    path('membros/editar_membro/<slug:slug>/atualizar_entregador/',views.atualizar_entregador,name='atualizar_entregador'),
    path('membros/detalhe/<slug:slug>', views.detalhe, name='detalhe'),
    path('entregas/apagar_entrega/<int:id>',views.apagar_entrega,name='apagar_entrega')
]