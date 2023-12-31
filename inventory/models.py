from django.db import models
from vendor.models import Vendor
from media import images

# Create your models here.
class Product(models.Model):
    vendor=models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField()
    datecreated=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField()






