
from rest_framework import serializers
from.models import CourseCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('category_id', 'category_title', 'category_short')

#class CategorySerializer(serializers.ModelSerializer):
#class Meta:
#model = Category
#fields = ['ct_id', 'ct_title']       