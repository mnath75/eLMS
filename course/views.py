
# Create your views here.
from django.shortcuts import render
from .serializers import CategorySerializer,CourseSerializer,SubjectSerializer
from rest_framework import viewsets
from .models import CourseCategory,Course,Subject
from rest_framework.response import Response
from django_filters import rest_framework as filters

class CategoryModelViewSet(viewsets.ModelViewSet):
  queryset = CourseCategory.objects.all()
  serializer_class = CategorySerializer



class CourseModelViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  filter_backends = (filters.DjangoFilterBackend,)
  filterset_fields = ['cr_categ']
  serializer_class = CourseSerializer  

class SubjectModelViewSet(viewsets.ModelViewSet):
  queryset = Subject.objects.all()
  filter_backends = (filters.DjangoFilterBackend,)
  filterset_fields = ['sub_course']
  serializer_class = SubjectSerializer 


 