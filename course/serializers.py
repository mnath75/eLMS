
from rest_framework import serializers
from.models import CourseCategory,Course
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('category_id', 'category_title', 'category_short')

#class CategorySerializer(serializers.ModelSerializer):
#class Meta:
#model = Category
#fields = ['ct_id', 'ct_title']  



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('cr_id','cr_title','cr_slug','cr_categ')     