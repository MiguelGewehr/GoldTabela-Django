from django.shortcuts import render
from home_page.models import Championship

def index(request):
    championships = Championship.objects.all()
    return render(request, 'home_page/index.html', {"cards": championships})

def register_championship(request):
    return render(request, 'home_page/register_championship.html')
