from django.db import models
# Create your models here.
class Reviews(models.Model):
    MODERATION_CHOICES=(("published","Published"),("rejected","Rejected"),("pending","Pending"),
                        )
    nameofProduct=models.CharField(max_length=32)
    rating=models.PositiveIntegerField()
    comment=models.TextField()
    datecreated=models.DateTimeField(auto_now_add=True)
    dateupdated=models.DateTimeField(auto_now=True)
    moderationStatus=models.CharField(max_length=32,choices=MODERATION_CHOICES)
    flagged=models.BooleanField(default=False)
    helpfulCount=models.PositiveIntegerField()
