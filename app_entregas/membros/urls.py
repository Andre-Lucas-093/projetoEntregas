from django.urls import path
from . import views

urlpatterns = [
    path('membros/', views.membros, name='membros'),
    path('membros/detalhe/<int:id>', views.detalhe, name='detalhe'),
]