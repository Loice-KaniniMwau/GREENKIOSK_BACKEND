from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_Name","last_Name"
    ,"email_Address"
    ,"phone_No",
    "account_password",
    "delivery_Location")
admin.site.register(Customer,CustomerAdmin)
