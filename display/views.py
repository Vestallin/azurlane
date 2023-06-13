from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django_tables2 import SingleTableView
from .models import Ship
from .table import ShipTable
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def showShip(request):
    table= Ship.objects.all()
    return render(request, 'ship.html', { 'table': table})
