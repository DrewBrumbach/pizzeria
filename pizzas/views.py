from django.shortcuts import render
from .models import Pizza, Topping
from django.http import Http404

# Create your views here.


def index(request):
    """the home page for pizzeria."""
    return render(request, "pizzas/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("text")

    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("-text")

    context = {"pizza": pizza, "toppings": toppings}

    return render(request, "pizzas/pizza.html", context)
