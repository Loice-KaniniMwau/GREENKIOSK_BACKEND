from django.contrib import admin

# Register your models here.
from .models import Reviews
class ReviewsAdmin(admin.ModelAdmin):
    list_display=("nameofProduct","rating","comment","helpfulCount","flagged","moderationStatus","dateupdated","datecreated")
admin.site.register(Reviews,ReviewsAdmin)

