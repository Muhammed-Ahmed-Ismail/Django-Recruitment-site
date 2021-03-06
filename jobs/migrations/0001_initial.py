# Generated by Django 4.0.5 on 2022-06-16 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('Modification_time', models.DateTimeField(auto_now=True)),
                ('Description', models.TextField(max_length=255)),
                ('status', models.CharField(choices=[('O', 'open'), ('IN', 'inprogress'), ('F', 'finished')], default='O', max_length=2)),
                ('image', models.CharField(default='https://dummyimage.com/200x300/000/ffffff', max_length=255)),
                ('applied_developer', models.ManyToManyField(blank=True, to='accounts.developer')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company')),
                ('tags', models.ManyToManyField(to='tags.tag')),
            ],
        ),
    ]
