from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Types(models.TextChoices):
        DEVELOPER = 'DEVELOPER'
        COMPANY = 'COMPANY'

    class Genders(models.TextChoices):
        MALE = 'MALE'
        FEMALE = 'FEMALE'

    email = models.EmailField("email address")
    user_type = models.CharField('type', max_length=10, choices=Types.choices)
    gender = models.CharField('gender', max_length=6, choices=Genders.choices)
    date_of_birth = models.DateField('date_of_birth', null=True)
    job = models.ManyToManyField('jobs.job')
    cv = models.FileField(upload_to='static/cv', null=True)
    tags = models.ManyToManyField('tags.tag')
    history = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=100, null=True)
    can_apply = models.BooleanField(default=True)
    notify_by_mail = models.BooleanField(null=True)
# class Developer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
