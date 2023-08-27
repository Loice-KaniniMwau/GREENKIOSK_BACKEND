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
     product_name=models.CharField(max_length=32,default="")
     product_price=models.IntegerField(default=1)
     product_quantity=models.IntegerField(default=1)
     product_image=models.ImageField(default="")
     notes=models.TextField()
     cartstatus=models.CharField(max_length=32,choices=STATUS_CHOICES)
     

