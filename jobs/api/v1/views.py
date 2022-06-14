from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.api.v1.permissions import CompEditMyJopPermission
from jobs.models import Job
from jobs.api.v1.serializer import JobSerializer
from rest_framework import status


@api_view(['GET'])
def index(request):
    try:
        queryset = Job.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": "No jobs exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def detail(request, job_id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        actor = Job.objects.get(id=job_id)
        serializer = JobSerializer(actor, many=False)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except:
        response['data'] = {'server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['POST'])
def create(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = serializer.errors
    except:
        response['data'] = {'server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, CompEditMyJopPermission])
def edit(request, job_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        movie_instance = Job.objects.get(id=job_id)

        if request.method == 'PUT':
            serializer = JobSerializer(instance=movie_instance, data=request.data)
        else:  # PATCH
            serializer = JobSerializer(instance=movie_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = serializer.errors
    except:
        response['data'] = {'bad request'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(**response)


@api_view(['DELETE'])
def delete(request, actor_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        Job.objects.get(id=actor_id).delete()
        response['data'] = {'deleted'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_404_NOT_FOUND
    finally:
        return Response(**response)
