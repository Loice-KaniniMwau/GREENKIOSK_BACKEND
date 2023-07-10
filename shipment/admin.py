from django.contrib import admin
from .models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display=("shipment_method","delivery_date","signature_required","delivery_status")


admin.site.register(Shipment,ShipmentAdmin)

# Register your models here.


# from .models import ShoppingCart
# class ShoppingCartAdmin(admin.ModelAdmin):
#     list_display=("notes","cartstatus")
#     def display_total_amount(self, obj):
#         return obj.calculate_total_amount()

#     display_total_amount.short_description = 'Total Amount'
# admin.site.register(ShoppingCart,ShoppingCartAdmin)

