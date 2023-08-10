from django.contrib import admin

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("image","first_Name","last_Name"
    ,"email_Address"
    ,"phone_No",
    "account_password",
    "delivery_Location")
admin.site.register(Customer,CustomerAdmin)
