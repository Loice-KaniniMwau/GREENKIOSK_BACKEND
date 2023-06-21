from django.db import models

# Create your models here.
class Delivery(models.Model):
    deliverystatus=(
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('delivered', 'Delivered'),
        )
    recepientname=models.CharField(max_length=32)
    recepientphone=models.CharField(max_length=32) 
    deliveryadress=models.CharField(max_length=32) 
    deliverydate=models.DateTimeField(auto_now_add=True) 
    deliverystatus=models.CharField(max_length=32,choices=deliverystatus)

