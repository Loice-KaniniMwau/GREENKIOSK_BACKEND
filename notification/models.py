from django.db import models
from customer.models import Customer
from order.models import Order
from inventory.models import Product

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
