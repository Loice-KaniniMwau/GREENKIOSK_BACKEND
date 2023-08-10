from django.contrib import admin
from .models import Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display=("content","timestamp")
admin.site.register(Notification,NotificationAdmin)




# Register your models here.
# user = models.ForeignKey(Customer,on_delete=models.CASCADE)
