from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Membro

def membros(request):
    todos_membros = Membro.objects.all().values()
    
    template = loader.get_template('todos_membros.html')
    context = {
    'todos_membros': todos_membros,
  }
    return HttpResponse(template.render(context,request))

def detalhe(request,id):
    meumembro = Membro.objects.get(id=id)
    
    template = loader.get_template('detalhe.html')
    context = {
    'meumembro': meumembro,
    }
    return HttpResponse(template.render(context,request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())