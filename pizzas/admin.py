from django.contrib import admin

# Register your models here.
# Now the admin part of the server allows you to edit the attributes you defined in the model

from .models import Pizza
from .models import Topping
from .models import Comment

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)
