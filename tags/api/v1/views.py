from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.api.v1.permissions import CompEditMyJopPermission
from tags.models import Tag
from .serializers import TagSerializer
from rest_framework import status


@api_view(['GET'])
@permission_classes([])
def index(request):
    try:
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": "No jobs exist"}, status=status.HTTP_404_NOT_FOUND)