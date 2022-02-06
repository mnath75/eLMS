
from rest_framework import serializers
from.models import Categorys

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = ('category_id', 'category_title', 'category_slug')

#class CategorySerializer(serializers.ModelSerializer):
#class Meta:
#model = Category
#fields = ['ct_id', 'ct_title']       