from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=32)
    phoneNumber=models.CharField(max_length=32)
    emailAddress=models.EmailField()
    location=models.CharField(max_length=32)
    shopname=models.CharField(max_length=32)








