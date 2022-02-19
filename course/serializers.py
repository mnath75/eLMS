
from rest_framework import serializers
from.models import CourseCategory,Course,Subject
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
        fields = ('cr_id','cr_title','cr_categ') 

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('sub_id','sub_title','sub_course')