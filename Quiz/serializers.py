from rest_framework import serializers
from .models import Qtype
class QtypeSerializer(serializers.ModelSerializer):
 class Meta:
  model = Qtype
  fields = ['qt_id', 'qt_title']