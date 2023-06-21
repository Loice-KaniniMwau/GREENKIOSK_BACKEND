from django.db import models


# Create your models here.
class ShoppingCart(models.Model):
     STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
        )
     nameofproduct=models.CharField(max_length=32)
     totalitems=models.PositiveIntegerField()
     product_description=models.TextField()
     priceofeach=models.DecimalField(max_digits=32,decimal_places=2)
     totalamount=models.DecimalField(max_digits=32,decimal_places=2)
     cartstatus=models.CharField(max_length=32,choices=STATUS_CHOICES)
     def calculate_total_amount(self):
        self.totalamount = self.totalitems * self.priceofeach
        self.save()


