
from django.urls import path
from .views import ValidatePhoneSendOTP,ValidateOTP,Register

urlpatterns = [

    path('validate_phone/',ValidatePhoneSendOTP.as_view()),
    path('validate_otp/',ValidateOTP.as_view()),
    path('Register/',Register.as_view()),
]