from django.shortcuts import render
from firstapp.models import Pizza

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'firstapp/home.html', { 'insert': 'Вставка из view.py', 'pizzas': pizzas })
