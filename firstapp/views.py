from django.shortcuts import render, get_object_or_404
from firstapp.models import Pizza

from  firstapp.forms import OrderForm

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'firstapp/home.html', {'insert': 'Вставка из view.py', 'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = OrderForm(initial={'pizza':pizza})
    return render(request, 'firstapp/pizza_detail.html', {
        'pizza': pizza,
        'form': form,
    })
