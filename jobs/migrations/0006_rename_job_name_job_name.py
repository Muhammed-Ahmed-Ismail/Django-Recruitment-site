# Generated by Django 4.0.4 on 2022-06-10 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_job_name_job_job_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_name',
            new_name='name',
        ),
    ]
