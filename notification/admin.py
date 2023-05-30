from django.contrib import admin
from django.dispatch.dispatcher import NO_RECEIVERS


from .models import Notification, UserObj

# Register your models here.
admin.site.register(Notification)
admin.site.register(UserObj)