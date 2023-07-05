from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("order_number","customer_name","customer_email","customer_phoneNumber","order_date","order_status")
admin.site.register(Order,OrderAdmin)

