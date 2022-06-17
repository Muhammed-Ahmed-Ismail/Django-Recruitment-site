from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.api.v1.permissions import CompEditMyJopPermission, CompCreateJobPermission, DevApplyForJobPermission, \
    DevCanApply
from accounts.models import Developer
from jobs.models import Job

from jobs.api.v1.serializer import JobSerializer, JobCreateEditSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    try:
        queryset = Job.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": "No jobs exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated , CompCreateJobPermission])
def my_jobs(request):
    try:
        queryset = request.user.company.job_set.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": "No jobs exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([])
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
@permission_classes([IsAuthenticated, CompCreateJobPermission])
def create(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        serializer = JobCreateEditSerializer(data=request.data)
        print(request.data)
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


#     query_set=Job.objects.create(
#         # status='O',
#         name=body['name'],
#         Description= body['Description'],
#         # Tags = body['tags'],
#         # developer = body['developer'],
#         ## ^^ notify accepted developer and all the others notify with rejection
#         # created_by = body['created_by']
#     )
#     serializer=JobSerializer(query_set)
# ##########send notification to all developers who have matched tags
#     notifications = Notifications()
#     # notifications.send_mail_to_devs_w_matching_tags(Tags)
#     return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, CompEditMyJopPermission])
def edit(request, job_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        job_instance = Job.objects.get(id=job_id)

        if request.method == 'PUT':
            serializer = JobCreateEditSerializer(instance=job_instance, data=request.data)
        else:  # PATCH
            serializer = JobCreateEditSerializer(instance=job_instance, data=request.data, partial=True)

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
@permission_classes([IsAuthenticated, CompEditMyJopPermission])
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


@api_view(['POST'])
@permission_classes([IsAuthenticated, DevApplyForJobPermission, DevCanApply])
def apply(request, job_id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        job = Job.objects.get(id=job_id)
        applying_developer = request.user.developer
        applying_developer.apply(job)
        response['data'] = {'Application succeeded'}
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
@permission_classes([IsAuthenticated, CompEditMyJopPermission])
def assign(request, job_id, dev_id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        job = Job.objects.get(id=job_id)
        developer = job.applied_developer.get(id=dev_id)

        job.assign_to_developer(developer)
        response['data'] = {'Developer has been sent a mail for acceptance'}
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except:
        response['data'] = {'server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)
