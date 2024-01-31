from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def menu(request):
    return HttpResponse('<h1>This future menu page</h1>')


def menu_category(request, category:int):
    return HttpResponse(f'<h1>This future menu_category {category} page</h1>')


def menu_dish(request, category:int, dish:int):
    return HttpResponse(f'<h1>This future menu_category {category}, dish - {dish} page</h1>')