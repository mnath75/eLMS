"""learnoskill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from Quiz import views as vi
router = DefaultRouter()
from course import views
from exam import views as ex
from account import views as ac
from course2 import views as ba

router.register('categoryapi', views.CategoryModelViewSet, basename='category')
router.register('courseapi', views.CourseModelViewSet, basename='course')
router.register('subjectapi', views.SubjectModelViewSet, basename='subject')
router.register('topicapi', views.TopicModelViewSet, basename='topic')
router.register('Qtype', vi.QtypeModelViewSet, basename='qtype')
router.register('questions', ex.ViewsetQuestion, basename='question')
router.register('answers', ex.ViewsetAnswer, basename='answer')
router.register('userprofile',ac.UserView,basename="profile") 
router.register('categorybatch',ba.CategoryModelViewSet,basename="catbatch") 
router.register('coursebatch',ba.CourseModelViewSet,basename="coursebatch") 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('account.urls')),
    path('course/',include('course.urls')),
    path('quiz/',include('Quiz.urls')),
    path('exam/',include('exam.urls')),
    path('course2/',include('course2.urls')),
    path('', include(router.urls))
]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)