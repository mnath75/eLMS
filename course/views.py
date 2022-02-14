
# Create your views here.
from django.shortcuts import render
from .serializers import CategorySerializer,CourseSerializer
from rest_framework import viewsets
from .models import CourseCategory,Course

class CategoryModelViewSet(viewsets.ModelViewSet):
  queryset = CourseCategory.objects.all()
  serializer_class = CategorySerializer



class CourseModelViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer  