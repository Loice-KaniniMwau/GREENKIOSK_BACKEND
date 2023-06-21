from django.contrib import admin

# Register your models here.
from .models import Categories
class CategoriesAdmin(admin.ModelAdmin):
    list_display=("category_name","category_type","quantity_stocked")
admin.site.register(Categories,CategoriesAdmin)
