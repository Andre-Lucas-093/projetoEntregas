from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.utils.text import slugify
from datetime import date, timedelta,datetime
from .models import Membro,Entrega
from .forms import EntregaForm

DIAS_PT = {
    "Monday": "Segunda",
    "Tuesday": "Terça",
    "Wednesday": "Quarta",
    "Thursday": "Quinta",
    "Friday": "Sexta",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

def membros(request):
    todos_membros = Membro.objects.all().order_by('id').values()
    
    template = loader.get_template('todos_membros.html')
    context = {
    'todos_membros': todos_membros,
  }
    return HttpResponse(template.render(context,request))

def detalhe(request,slug):
    meumembro = Membro.objects.get(slug=slug)
    
    template = loader.get_template('detalhe.html')
    context = {
    'meumembro': meumembro,
    }
    return HttpResponse(template.render(context,request))

def editar_membro(request,slug):
    meumembro = Membro.objects.get(slug=slug)
    template = loader.get_template('editar_membro.html')

    context = {
    'meumembro': meumembro,
    'slug' :slug
    }
    return HttpResponse(template.render(context,request))

def atualizar_entregador(request,slug):
        if request.method == 'POST' and request.POST.get('_method') == 'PUT':  
            meumembro = Membro.objects.get(slug=slug)
            codigo = request.POST.get('codigo')
            entregador = request.POST.get('entregador')

            if codigo and entregador:
                meumembro.codigo = codigo
                meumembro.nome = entregador
                meumembro.slug = slugify(f'{codigo}-{entregador}')
                meumembro.save()
                return redirect('membros')
            
def excluir_membro(request,slug):
        meumembro = Membro.objects.get(slug=slug)

        meumembro.delete()
        return redirect('membros')

def apagar_entrega(request,id):
    entrega = Entrega.objects.get(id=id)

    entrega.delete()
    return redirect('entregas')

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def get_semana():
    hoje = date.today()
    segunda = hoje - timedelta(days=hoje.weekday())
    return [segunda + timedelta(days=i) for i in range(6)]  # Segunda a Sábado

def entregas(request):
    if request.method == "POST":
        form = EntregaForm(request.POST)
        
        if form.is_valid():
            entrega = form.save(commit=False)
            # Pega a data enviada via hidden input (string no formato 'YYYY-MM-DD')
            data_entrega_str = request.POST.get('data_entrega')
            data_convertida = datetime.strptime(data_entrega_str, "%B %d, %Y").date()
            print(data_entrega_str)
            if data_convertida:
                entrega.data_entrega = data_convertida
            else:
                entrega.data_entrega = date.today()  # fallback
            form.save()
            return redirect('entregas')
    else:
        form = EntregaForm()

    dias = get_semana()
    agenda = []
    
    for dia in dias:
        nome_ingles = dia.strftime('%A')
        nome_pt = DIAS_PT.get(nome_ingles, nome_ingles)
        entregas = Entrega.objects.filter(data_entrega=dia).select_related("vendedor")
        agenda.append({
            "data": dia,
            "entregas": entregas,
            "nome_dia": nome_pt
        })

    return render(request, "entregas.html", {
        "agenda": agenda,
        "form": form
    })

    return template.render(request,context)

def adicionar_membro(request):
    return render(request, 'adicionar_membro.html')

def cadastrar_entregador(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        entregador = request.POST.get('entregador')

        if codigo and entregador:
            novo_membro = Membro(codigo = codigo, nome=entregador)
            novo_membro.slug = slugify(f'{codigo}-{entregador}')
            novo_membro.save()
            return redirect('membros')  # ou outra URL que preferir

    return render(request, 'adicionar_membro.html')