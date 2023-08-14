from django.shortcuts import render
from .models import Ship
def showShip(request):
    table= Ship.objects.all()
    return render(request, 'ship.html', { 'table': table})

def instruct(request):
    selection = Ship.objects.all().values("faction").distinct()
    context = {'selection': selection}
    if request.method == "POST":
        result = request.POST.getlist('ships')
        if result:
            table = Ship.objects.filter(faction__in=result)
            context['post'] = table
            print(request.POST.getlist("ships"))
    return render(request, 'filter.html', context)

