from django.db import models

# Create your models here.
class Customer(models.Model):
    first_Name=models.CharField(max_length=32)
    last_Name=models.CharField(max_length=32)
    email_Address=models.EmailField()
    phone_No=models.CharField(max_length=32)
    account_password=models.CharField(max_length=32)
    delivery_Location=models.CharField(max_length=32)
    

    


   













    
