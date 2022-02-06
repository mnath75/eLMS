
# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import  Categorys
from .serializers import  CategoryListSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories=Categorys.objects.all()
    serializer=CategoryListSerializer(categories, many=True)
    print("heeeeeeeeeee")
    return Response(serializer.data)