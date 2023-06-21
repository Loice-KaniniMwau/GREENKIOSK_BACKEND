from django.contrib import admin

# Register your models here.
from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("recepientname",
    "recepientphone",
    "deliveryadress",
    "deliverydate",
    "deliverystatus")

    
admin.site.register(Delivery,DeliveryAdmin)

