from django.urls import path, re_path
from app_web.views.register import Register
from app_web.views.getinfo import GetInfo
from app_web.views.test import test
from app_web.views.query import Query
from app_web.views.getquery import GetQuery
from app_web.views.index import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('userregister/',Register.as_view(),name="register"),
    path('api/token/',TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/',TokenRefreshView.as_view(), name="token_regresh"),
    path('api/token/verify/',TokenVerifyView.as_view(), name="token_verify"),
    path('getinfo/',GetInfo.as_view(), name="getinfo"),
    path('query/',Query.as_view(), name="query"),
    path('getquery/',GetQuery.as_view(), name="getquery"),
    re_path(r".*",index,name="index"),
]
