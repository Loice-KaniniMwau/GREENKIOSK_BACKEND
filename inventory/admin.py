from django.contrib import admin

# Register your models here.
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","description","datecreated","date_updated")
admin.site.register(Product,ProductAdmin)


