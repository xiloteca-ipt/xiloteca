from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('base.html')
    context = {
        'message': "Hello, world!",
    }
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('base.html')
    context = {
        'message': "Página de busca com filtros",
    }
    return HttpResponse(template.render(context, request))

def results(request):
    template = loader.get_template('base.html')
    context = {
        'message': "Nenhum resultado encontrado.",
    }
    return HttpResponse(template.render(context, request))

def details(request):
    template = loader.get_template('base.html')
    context = {
        'message': "Esta é uma página de detalhes das madeiras",
    }
    return HttpResponse(template.render(context, request))
