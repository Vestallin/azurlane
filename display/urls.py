from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showShip, name='table'),
    path('filter', views.instruct, name="filter"),
]