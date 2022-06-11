from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateCompanySerializer, CreateDeveloperSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes([])
def signup(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    if (request.data['user_type'] == 'DEVELOPER'):
        serializer = CreateDeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_201_CREATED

        else:
            response['data'] = serializer.errors
    elif (request.data['user_type'] == 'COMPANY'):
        serializer = CreateCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_201_CREATED

        else:
            response['data'] = serializer.errors
    return Response(**response)
