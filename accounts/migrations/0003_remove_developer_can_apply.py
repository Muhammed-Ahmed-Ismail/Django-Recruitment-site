# Generated by Django 4.0.5 on 2022-06-11 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_date_of_birth_user_gender_user_user_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='can_apply',
        ),
    ]
