from django.contrib import admin

# Register your models here.
from .models import Product_Cart
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display=("product_name","product_price","product_quantity","product_image","date_added")
    def display_total_amount(self, obj):
        return obj.calculate_total_amount()

    display_total_amount.short_description = 'Total Amount'
admin.site.register(Product_Cart,ShoppingCartAdmin)
