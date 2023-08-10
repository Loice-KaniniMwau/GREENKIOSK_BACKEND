from django.db import models
from customer.models import Customer

# Create your models here.
class Delivery(models.Model):
    deliverystatus=(
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('delivered', 'Delivered'),
        )
    # recepientname=models.CharField(max_length=32)
    recepientname=models.OneToOneField(Customer,on_delete=models.CASCADE,null=True,default="")
    recepientphone=models.CharField(max_length=32) 
    deliveryadress=models.CharField(max_length=32) 
    deliverydate=models.DateTimeField(auto_now_add=True) 
    deliverystatus=models.CharField(max_length=32,choices=deliverystatus)

