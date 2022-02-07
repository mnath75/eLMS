
# Create your views here.
from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework import viewsets
from .models import CourseCategory

class CategoryModelViewSet(viewsets.ModelViewSet):
  queryset = CourseCategory.objects.all()
  serializer_class = CategorySerializer