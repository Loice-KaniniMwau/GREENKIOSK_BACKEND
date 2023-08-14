from django.contrib import admin
from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display=(
    "recepientphone",
    "deliveryadress",
    "deliverydate",
    "deliverystatus")

    
admin.site.register(Delivery,DeliveryAdmin)

# recepientname=models.CharField(max_length=32)
#     recepientphone=models.CharField(max_length=32) 
#     deliveryadress=models.CharField(max_length=32) 
#     deliverydate=models.DateTimeField(auto_now_add=True) 
#     deliverystatus=models.CharField(max_length=32,choices=deliverystatus)


# # 