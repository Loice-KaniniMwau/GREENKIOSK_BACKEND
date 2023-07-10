from django.db import models
from order.models import Order

# Create your models here.
class Shipment(models.Model):
    SHIPMENT_CHOICES=(
        ("in-store pickup","in-store pickup"),("home delivery","home delivery")
    ,)
    DELIVERY_CHOICES=(("out for delivery","out for delivery"),("delivered","Delivered"),("delayed","Delayed"),)
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    shipment_method=models.CharField(max_length=32,choices=SHIPMENT_CHOICES)
    delivery_date=models.DateTimeField()
    delivery_status=models.CharField(max_length=32,choices=DELIVERY_CHOICES)
    signature_required=models.BooleanField()



#   user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    
# shipment_number = models.CharField(max_length=32, unique=True)
    # order = models.OneToOneField(Order, on_delete=models.CASCADE)
    # shipment_method = models.CharField(max_length=32)
    # delivery_date = models.DateField()
    # delivery_time_slot = models.CharField(max_length=32)
    # tracking_url = models.URLField()
    # delivery_driver = models.CharField(max_length=64)
    # delivery_status = models.CharField(max_length=16)
    # delivery_instructions = models.TextField(blank=True)
    # packaging_type = models.CharField(max_length=32)
    # weight = models.DecimalField(max_digits=10, decimal_places=2)
    # signature_required = models.BooleanField()

# 

