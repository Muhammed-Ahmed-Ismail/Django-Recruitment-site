# Generated by Django 4.0.4 on 2022-06-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Tags',
            field=models.ManyToManyField(to='tags.tag'),
        ),
    ]
