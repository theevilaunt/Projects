from django.contrib import admin

# Register your models here.

from pizzas.models import Pizza, Topping, Pizza_Topping
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Pizza_Topping)
