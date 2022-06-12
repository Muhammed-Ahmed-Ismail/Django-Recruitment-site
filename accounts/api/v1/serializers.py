from rest_framework import serializers
from django.contrib.auth import get_user_model
from tags.api.v1.serializers import TagSerializer

from accounts.models import Developer,Company

User = get_user_model()


#
# class CreateCompanySerializer(serializers.Serializer):
#     pass


class CreateUserSerializer(serializers.ModelSerializer):
    # company = CreateCompanySerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_type', 'gender', 'date_of_birth']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            },
            'date_of_birth': {
                'required': True
            }
        }

    def create(self, validated_data):
        user = User(username=validated_data['username'],
                    email=validated_data['email'],
                    gender=validated_data['gender'],
                    user_type=validated_data['user_type'],
                    date_of_birth=validated_data['date_of_birth'])

        # user = User(**validated_data)
        print(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # user.tags.set(validated_data['tags'])

        return user


class CreateDeveloperSerializer(serializers.ModelSerializer):
    # user = CreateUserSerializer(read_only=True)

    class Meta:
        model = Developer
        fields = ['cv']
        extra_kwargs = {
            'cv': {
                'required': True
            },
        }
        # depth = 1

    def create(self, validated_data):
        developer = Developer(
            cv=validated_data['cv'],

        )

        # user = User(**validated_data)
        print('frrsd')
        # user.set_password(validated_data['password'])
        # developer.user.set(validated_data['user'])
        developer.save()
        # developer.tags.set(validated_data['tags'])

        return developer


class CreateCompanySerializer(serializers.ModelSerializer):
    # history = serializers.CharField(required=True, max_length=500)
    # address = serializers.CharField(required=True, max_length=100)

    # password = serializers.

    class Meta:
        model = Company
        fields = ['history', 'address']
        extra_kwargs = {

            'history': {
                'required': True,

            },
            'address': {
                'required': True,

            },

        }

    def create(self, validated_data):
        company = Company(
                    history=validated_data['history'],
                    address=validated_data['address'],
                   )

        # user = User(**validated_data)
        print(validated_data)
        # user.set_password(validated_data['password'])
        company.save()
        return company
