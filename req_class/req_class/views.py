from django.shortcuts import render
from django.http import HttpResponse

def minha_visualizacao(request):
    return HttpResponse("Olá, mundo!")
