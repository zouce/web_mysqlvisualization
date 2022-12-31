from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from app_web.models import Testtable
import json, time

class Query(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self, request):
        print('==================')
        #print(request.body.decode())
        data = request.POST
        print(data['code[_value]'])
        print("sleep")
        #code = data['code']
        #print(code)
        query_content = [{'id':1,'col5':'11ds1','col2':'2fsf22','col3':'333'},{'id':2,'col5':'111','col2':'222','col3':'333'},{'id':3,'col5':'111','col2':'222','col3':'333'}]
        query_content_title = ['col5','col2','col3']
        res = {'query_id':4,'query_content':query_content,'query_content_title':query_content_title}
        return Response(res)
