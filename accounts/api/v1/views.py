import profile
from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateCompanySerializer, CreateDeveloperSerializer, CreateUserSerializer, UserSerializerForDeveloper, UserSerializerForCompany
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from accounts.models import Developer,Company

User = get_user_model()

@api_view(['POST'])
@permission_classes([])
def signup(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    # print(request.data)
    if (request.data['user_type'] == 'DEVELOPER'):

        serializer = CreateUserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():

            developer_serializer = CreateDeveloperSerializer(data=request.data)
            print(developer_serializer.is_valid())
            if developer_serializer.is_valid():
                developer = developer_serializer.save()
                user = serializer.save()
                developer.user = user
                developer.save()
                print(request.data['tags'])
                # developer.tags.set(re)
                response['data'] = [serializer.data, developer_serializer.data]
                response['status'] = status.HTTP_201_CREATED
            else:
                response['data'] = developer_serializer.errors
        else:
            response['data'] = serializer.errors


    elif (request.data['user_type'] == 'COMPANY'):
        serializer = CreateUserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():

            # print(user)
            company_serializer = CreateCompanySerializer(data=request.data)
            print(company_serializer.is_valid())
            if company_serializer.is_valid():
                company = company_serializer.save()
                user = serializer.save()
                company.user = user
                company.save()
                response['data'] = [serializer.data, company_serializer.data]
                response['status'] = status.HTTP_201_CREATED
            else:
                response['data'] = company_serializer.errors
        else:
            response['data'] = serializer.errors
    print(Response(**response))
    return Response(**response)

@api_view(['GET'])
def getProfile(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    profile = User.objects.get(pk = request.user.id)
    print(profile)

    if(profile.user_type == 'DEVELOPER'):
        serial = UserSerializerForDeveloper(profile, many=False)
        return Response(data=serial.data, status=status.HTTP_200_OK)

    elif(profile.user_type == 'COMPANY'):
        serial = UserSerializerForCompany(profile, many=False)
        return Response(data=serial.data, status=status.HTTP_200_OK)
    return Response(**response)
    