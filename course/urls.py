
from django.urls import path
from .views import get_categories
from . import views


urlpatterns = [
   
     path('cat/', views.get_categories,name='cat'),
   
]