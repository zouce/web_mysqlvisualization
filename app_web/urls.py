from django.urls import path
from app_web.views.register import Register
from app_web.views.getinfo import GetInfo
from app_web.views.test import test
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('',test),
    path('register/',Register.as_view(),name="register"),
    path('api/token/',TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/',TokenRefreshView.as_view(), name="token_regresh"),
    path('api/token/verify/',TokenVerifyView.as_view(), name="token_verify"),
    path('getinfo/',GetInfo.as_view(), name="getinfo"),
]
