from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    # company = CreateCompanySerializer()

    class Meta:
        model = Tag
        fields = '__all__'
