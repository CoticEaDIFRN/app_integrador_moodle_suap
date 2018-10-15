from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def sincronizacao(request):
    template = loader.get_template('sincronizacao.html')
    response_body = template.render()
    return HttpResponse(response_body)