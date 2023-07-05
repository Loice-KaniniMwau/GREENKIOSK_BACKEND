from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("nameofPayee","amount","paymentStatement","paymentmethod","paymentstatus","datepaid")
admin.site.register(Payment,PaymentAdmin)

