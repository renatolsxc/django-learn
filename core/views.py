from django.shortcuts import render
from .models import Produto
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

def index(request):
    #print(dir(request))
    #print(f'Metodo: {request.method}')
    #print(f'Headers: {request.headers}')
    #print(f"User Agent: {request.headers['User-Agent']}")
    #print(f"User: {request.user}")
    #print(dir(request.user))
    #print(f"LstName: {request.user.last_name}")
    #print(f"E-mail user: {request.user.email}")

    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário Logado'

    context = {
        'curso': 'Programação Web com Djang framework',
        'outro': 'Outra Variável',
        'logado': teste,
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(render, 'contato.html')


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod,
    }
    return render(render, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html, charset=utf-8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html, charset=utf-8', status=500)


