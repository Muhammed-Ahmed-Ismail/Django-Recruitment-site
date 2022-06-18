from rest_framework import serializers
from jobs.models import Job


# from django.db.models.fields. import TextField
from tags.models import Tag


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        depth = 2


class JobApplicationSeriaizer(serializers.Serializer):
    class Meta:
        fields = ['developer_id', '']


class Tagserializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id']


class JobCreateEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
