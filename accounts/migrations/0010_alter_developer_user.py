# Generated by Django 4.0.5 on 2022-06-11 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_user_cv_remove_user_job_remove_user_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
