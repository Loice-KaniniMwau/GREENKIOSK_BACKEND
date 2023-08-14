from django.db import models
from django.contrib.auth.models import User
from payment.models import Payment

# Create your models here.
class Delivery(models.Model):
    deliverystatus=(
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('delivered', 'Delivered'),
        )
    payment=models.OneToOneField(Payment,on_delete=models.CASCADE,default="")
    recepientphone=models.CharField(max_length=32) 
    deliveryadress=models.CharField(max_length=32) 
    deliverydate=models.DateTimeField(auto_now_add=True) 
    deliverystatus=models.CharField(max_length=32,choices=deliverystatus)

# from django.contrib.auth.models import User

# from django.contrib.auth.models import User
