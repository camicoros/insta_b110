from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>ПРИВЕТ!!!</h1><p>Как дела?</p>")


def about(request):
    return HttpResponse("О нас")


def contact(request):
    return HttpResponse("Контакты")


def blog(request):
    return HttpResponse("Статьи")