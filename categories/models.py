from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name=models.CharField(max_length=32)
    category_type=models.CharField(max_length=32)
    quantity_stocked=models.PositiveIntegerField()


