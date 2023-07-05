from django.db import models

# Create your models here.
class Payment(models.Model):
    PAYMENT_METHODS=(("mpesa","Mpesa"),("cash","Cash"),)
    PAYMENT_STATUS=(("approved","Approved"),("pending","Pending"),("cancelled","Canclled"),)
    nameofPayee=models.CharField(max_length=32,default="")
    amount=models.DecimalField(default=0.00,max_digits=32,decimal_places=2)
    paymentmethod=models.CharField(max_length=32,choices=PAYMENT_METHODS)
    paymentstatus=models.CharField(max_length=32,choices=PAYMENT_STATUS)
    paymentStatement=models.TextField(default="")
    datepaid=models.DateTimeField(auto_now_add=True)
