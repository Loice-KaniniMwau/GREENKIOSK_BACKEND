from django.contrib import admin
from .models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display=("shipment_method","delivery_date","signature_required","delivery_status")


admin.site.register(Shipment,ShipmentAdmin)

# Register your models here.



