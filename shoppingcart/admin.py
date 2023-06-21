from django.contrib import admin

# Register your models here.
from .models import ShoppingCart
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display=("nameofproduct","totalitems","product_description","priceofeach","totalamount","cartstatus")
    def display_total_amount(self, obj):
        return obj.calculate_total_amount()

    display_total_amount.short_description = 'Total Amount'
admin.site.register(ShoppingCart,ShoppingCartAdmin)

