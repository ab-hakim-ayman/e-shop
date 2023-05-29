from django.contrib import admin

from .models import Wish, Cart, Order, OrderUpdate

# Register your models here.
admin.site.register(Wish)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderUpdate)