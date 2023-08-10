from django.contrib import admin
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("amount","paymentStatement","paymentmethod","paymentstatus","datepaid")
admin.site.register(Payment,PaymentAdmin)

#  nameofPayee=models.OneToOneField(User,on_delete=models.CASCADE)
    # amount=models.DecimalField(default=0.00,max_digits=32,decimal_places=2)
    # paymentmethod=models.CharField(max_length=32,choices=PAYMENT_METHODS)
    # paymentstatus=models.CharField(max_length=32,choices=PAYMENT_STATUS)
    # paymentStatement=models.TextField(default="")
    # datepaid=models.DateTimeField(auto_now_add=True)