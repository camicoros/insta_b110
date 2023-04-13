from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    print(request)
    print(request.GET)
    return HttpResponse("О нас")


def about_detail(request, user_id):
    print(request)
    print(request.GET)
    print(user_id)
    return HttpResponse(f"О пользователе {user_id}")


def my_date(request, selected_date):
    return HttpResponse(f"дата: {selected_date}")
