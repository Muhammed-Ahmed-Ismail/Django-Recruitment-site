from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jobs.models import Job
from jobs.api.v1.serializer import JobSerializer
from jobs.api.v1.Notifications import Notifications
def index(request):
    try:
        querySet=Job.objects.all()
        serializer=JobSerializer(querySet,many=True)
        return Response(serializer.data)
    except:
        return Response({"status":"No jobs exist"})

@api_view(['GET'])
def detail(request,id):
    try:
        querySet=Job.objects.get(pk=id)
        serializer=JobSerializer(querySet)
        return Response(serializer.data)
    except:
        return Response({"status":"Job doesn't exxit"})



@api_view(['POST'])
def create(request):
    serializer=JobSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data
    body=request.data

    query_set=Job.objects.create(
        # status='O',
        name=body['name'],
        Description= body['Description'],
        # Tags = body['tags'],
        # developer = body['developer'],
        ## ^^ notify accepted developer and all the others notify with rejection
        # created_by = body['created_by']
    )
    serializer=JobSerializer(query_set)
    notifications = Notifications()
    # notifications.send_mail_to_devs_w_matching_tags(Tags)
    return Response(serializer.data)

@api_view(['PUT'])
def edit(request,id):
    body=request.data
    name=body['name'],
    Description= body['description'],
    # Tags = body['tags'],
    developer = body['developer'],
    created_by = body['created_by']
    job = Job.objects.get(pk = id)
    job.name = name if name else job.name
    job.Description = Description if Description else job.Description
    # job.Tags = Tags if Tags else job.Tags
    job.developer = developer if developer else job.developer
    job.created_by = created_by if created_by else job.created_by
    job.save()
    serializer=JobSerializer(job)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,id):
    try:
        emp = Job.objects.get(pk = id)
        emp.delete()
    except :
        return Response({"status":"record does not exist"})
        
    return Response({"status":"Deleted Successfully"})
