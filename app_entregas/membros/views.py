from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Membro

def membros(request):
    todos_membros = Membro.objects.all().order_by('id').values()
    
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

def editar_membro(request,id):
    meumembro = Membro.objects.get(id=id)
    template = loader.get_template('editar_membro.html')

    context = {
    'meumembro': meumembro,
    'id' :id
    }
    return HttpResponse(template.render(context,request))

def atualizar_entregador(request,id):
        if request.method == 'POST' and request.POST.get('_method') == 'PUT':  
            meumembro = Membro.objects.get(id=id)
            codigo = request.POST.get('codigo')
            entregador = request.POST.get('entregador')

            if codigo and entregador:
                meumembro.codigo = codigo
                meumembro.nome = entregador
                meumembro.save()
                return redirect('membros')  # ou outra URL que preferir

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def teste(request):
    template = loader.get_template('teste.html')
    return HttpResponse(template.render())

def adicionar_membro(request):
    return render(request, 'adicionar_membro.html')

def cadastrar_entregador(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        entregador = request.POST.get('entregador')

        if codigo and entregador:
            novo_membro = Membro(codigo = codigo, nome=entregador)
            novo_membro.save()
            return redirect('membros')  # ou outra URL que preferir

    return render(request, 'adicionar_membro.html')