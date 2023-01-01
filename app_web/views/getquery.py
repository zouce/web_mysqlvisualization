from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from app_web.models import Record
from django.core import serializers
import json

class GetQuery(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self, request):
        user_id = request.user.id
        is_superuser = False;
        if len(User.objects.filter(id=user_id,is_superuser=True)) != 0:
            is_superuser = True
        data = request.POST
        query_id = int(data['query_id'])
        res = {}
        if query_id == 0:
            query_content_title = ['username','time']
            query_content = []
            if is_superuser:
                query_record = Record.objects.all().order_by('-time')
            else:
                query_record = Record.objects.filter(userid=user_id).order_by('-time')
            for query in query_record:
                query_content.append({'id':query.id,'username':User.objects.filter(id=user_id)[0].username, 'time':query.time.strftime("%Y-%m-%d %H:%M:%S")})
            res = {'query_content':query_content,'query_content_title':query_content_title}
        else:
            fileurl = '/home/zouce/web_mysqlvisualization/app_web/static/file/json' + str(query_id) + '.json'
            file_obj = open(fileurl,'r')
            res = json.load(file_obj)
            file_obj.close()
        return Response(res)
        #query_content = [{'id':1,'col1':'111','col2':'222','col3':'333'},{'id':2,'col1':'111','col2':'222','col3':'333'},{'id':3,'col1':'111','col2':'222','col3':'333'}]
        #query_content_title = ['col1','col2','col3']
        #return Response({'query_content':query_content,'query_content_title':query_content_title})
