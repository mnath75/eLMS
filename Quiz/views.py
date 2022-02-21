from django.shortcuts import render

# Create your views here.
from .models import Qtype
from .serializers import QtypeSerializer
from rest_framework import viewsets
import django_filters
from django_filters import rest_framework as filters
class QtypeModelViewSet(viewsets.ModelViewSet):
  queryset = Qtype.objects.all()
  serializer_class = QtypeSerializer