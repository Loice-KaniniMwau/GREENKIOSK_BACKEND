from django.db import models
from inventory.models import Product
from customer.models import Customer



# Create your models here.
class ShoppingCart(models.Model):
     STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
        )
     user = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
     product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
     quantity = models.PositiveIntegerField(null=True)
     notes=models.TextField()
     cartstatus=models.CharField(max_length=32,choices=STATUS_CHOICES)
     

