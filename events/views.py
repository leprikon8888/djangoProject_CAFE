from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def events(request):
    return HttpResponse('<h1>This events page</h1>')


def events_year(request, year):
    if year < 2024:
        return HttpResponse('<h1>We were closed</h1>')
    return HttpResponse(f'<h1>This events {year} page</h1>')

def events_year_month(request, year, month):
    if year < 2024:
        return HttpResponse('<h1>We were closed</h1>')
    return HttpResponse(f'<h1>This events {year}, {month} month </h1>')


def future_events(request):
    return HttpResponse('<h1>This future events page</h1>')