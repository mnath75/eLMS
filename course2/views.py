from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import batchCategory,batchCourse
from .serializers import batchCategorySerializer,batchCourseSerializer
from django_filters import rest_framework as filters

class CategoryModelViewSet(viewsets.ModelViewSet):
  queryset = batchCategory.objects.all()
  serializer_class = batchCategorySerializer

class CourseModelViewSet(viewsets.ModelViewSet):
  queryset = batchCourse.objects.all()
  filter_backends = (filters.DjangoFilterBackend,)
  filterset_fields = ['bcr_categ']
  serializer_class = batchCourseSerializer   