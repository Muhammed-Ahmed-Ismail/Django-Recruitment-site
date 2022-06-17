from django.db import models


# Create your models here.

class Notification(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)
