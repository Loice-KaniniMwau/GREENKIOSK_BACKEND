from django.db import models

# Create your models here.
class Payment(models.Model):
    PAYMENT_METHODS=(("mpesa","Mpesa"),("cash","Cash"),)
    PAYMENT_STATUS=(("approved","Approved"),("pending","Pending"),("cancelled","Canclled"),)
    # name=models.CharField(max_length=32)
    # userid=models.CharField(max_length=32)
    paymentmethod=models.CharField(max_length=32,choices=PAYMENT_METHODS)
    paymentstatus=models.CharField(max_length=32,choices=PAYMENT_STATUS)
    datepaid=models.DateTimeField(auto_now_add=True)
