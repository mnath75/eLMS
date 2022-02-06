
from rest_framework import serializers
from.models import Category

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_title', 'category_slug')

#class CategorySerializer(serializers.ModelSerializer):
 #class Meta:
  #model = Category
  #fields = ['ct_id', 'ct_title']       