# Generated by Django 4.0.5 on 2022-06-14 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='created_job',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='job',
        ),
    ]
