from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, default='tag', null=True)
    def __str__(self):
         return self.name