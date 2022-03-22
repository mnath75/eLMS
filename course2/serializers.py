
from rest_framework import serializers
from.models import batchCategory,batchCourse
from rest_framework import serializers


class batchCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = batchCategory
        fields = ('cat_id', 'cat_title', 'cat_short')

#class CategorySerializer(serializers.ModelSerializer):
#class Meta:
#model = Category
#fields = ['ct_id', 'ct_title']  



class batchCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = batchCourse
        fields = ('bcr_id','bcr_title','bcr_categ') 


