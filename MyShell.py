import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django

django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

p = Pizza.objects.get(id=1)

print("Pizza: " + str(p))

toppings = p.topping_set.all()

for topping in toppings:
    print("Topping: " + str(topping))
