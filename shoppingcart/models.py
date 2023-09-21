from django.db import models
from inventory.models import Product

class Product_Cart(models.Model):
    products= models.ManyToManyField(Product)
    product_name = models.CharField(max_length=32)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField()
   
    def add_product(self, product):
        self.products.add(product)
        self.save()
        return self
    def get_total(self):
        products= self.products.all()
        total=0
        for product in products:
            total+=product.price
        return total
    def remove_product(self,product):
         if product in self.products.all():
              self.products.remove(product)
              self.save()
         return self

class Meta:
        verbose_name_plural = "cart"








    
     
   

