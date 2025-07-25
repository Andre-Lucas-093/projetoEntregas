from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('membros/', views.membros, name='membros'),
    path('membros/detalhe/<int:id>', views.detalhe, name='detalhe'),
]