from django.contrib.auth.models import AbstractUser
# from jobs.models import Job
from django.db import models

from .Notifications import send_acceptance_mail, send_rejection_mail


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


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # job = models.ManyToManyField('jobs.job')
    cv = models.FileField(upload_to='static/cv', null=True)
    tags = models.ManyToManyField('tags.tag')
    can_apply = models.BooleanField(default=True)
    notify_by_mail = models.BooleanField(null=True, default=True)
    notifications = models.ManyToManyField('notifications.notification')

    def apply(self, job):
        self.can_apply = False
        job.add_new_application(self)
        job.save()
        self.save()

    def free(self):
        self.can_apply = True
        self.save()

    def get_accepted(self):
        print('getaccepted',self.user.email)
        send_acceptance_mail(self.user.email)
        pass

    def get_rejected(self):
        self.free()
        send_rejection_mail(self.user.email)

    def notify(self):
        if not self.notify_by_mail:
            return
        pass

    def __str__(self):
        return self.user.username


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    history = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
