from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('teste/',views.teste, name='teste'),
    path('membros/', views.membros, name='membros'),
    path('membros/adicionar_membro/',views.adicionar_membro, name='adicionar_membro'),
    path('membros/adicionar_membro/cadastrar_entregador/',views.cadastrar_entregador, name='cadastrar_entregador'),
    path('membros/editar_membro/<int:id>',views.editar_membro,name='editar_membro'),
    path('membros/editar_membro/<int:id>/atualizar_entregador/',views.atualizar_entregador,name='atualizar_entregador'),
    path('membros/detalhe/<int:id>', views.detalhe, name='detalhe'),
]