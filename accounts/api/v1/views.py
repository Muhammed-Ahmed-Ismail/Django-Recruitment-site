from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateCompanySerializer, CreateDeveloperSerializer, CreateUserSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes([])
def signup(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    print(request.data)
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
