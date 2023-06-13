from django.shortcuts import render
from .models import Ship

def showShip(request):
    table= Ship.objects.all()
    return render(request, 'ship.html', { 'table': table})
