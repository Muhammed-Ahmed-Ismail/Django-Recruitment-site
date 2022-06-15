from rest_framework import serializers
from jobs.models import Job


# from django.db.models.fields. import TextField


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        depth = 2


class JobCreateEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('name', 'Description', 'image', 'created_by', 'status',)
