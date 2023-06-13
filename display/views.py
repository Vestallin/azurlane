from django.shortcuts import render

# Create your views here.
from django_tables2 import SingleTableView
from .models import Ship
from .table import ShipTable

class ShipListView(SingleTableView):
    model = Ship
    table_class = ShipTable
    template_name = 'ship.html'
