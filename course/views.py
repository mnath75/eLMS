
# Create your views here.
from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework import viewsets
from .models import Category

class CategoryModelViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer