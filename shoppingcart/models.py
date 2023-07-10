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
      # products=models.ManyToMany(Inventory)
     customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
   #   products=models.ManyToManyField(Product)
   #   nameofproduct=models.CharField(max_length=32)
   #   totalitems=models.PositiveIntegerField()
     notes=models.TextField()
   #   priceofeach=models.DecimalField(max_digits=32,decimal_places=2)
   #   totalamount=models.DecimalField(max_digits=32,decimal_places=2)
     cartstatus=models.CharField(max_length=32,choices=STATUS_CHOICES)
     def calculate_total_amount(self):
        self.totalamount = self.totalitems * self.priceofeach
        self.save()


