from rest_framework import serializers
from jobs.models import Job


# from django.db.models.fields. import TextField


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

#         [
#         'name',
#         'creation_time',
#         'Modification_time',
#         'Description',
#         # 'tags' ,
#         # 'applied_developers',
#         'developer',
#         'created_by' ,
#         'status' ,
# ]
