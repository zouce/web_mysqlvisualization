from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from app_web.models import Testtable, Record, HIGGS
from django.core import serializers
from django.db import connection
import json, time, os, datetime
import pandas as pd

class Query(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self, request):
        user_id = request.user.id
        data = request.POST
        code = str(data['code'])
        code = code.lower()
        code = code.replace('higgs','app_web_higgs')
        if(code.find("limit") == -1):
            code = code + " limit 100"
        cursor = connection.cursor()
        cursor.execute(code)
        raw = cursor.fetchall()
        query_content_title = [desc[0] for desc in cursor.description]
        query_content = []
        num = 1
        for item in raw:
            tmap = dict(zip(query_content_title,item))
            tmap['id'] = num
            num += 1
            query_content.append(tmap)
        folderurl = '/home/zouce/web_mysqlvisualization/app_web/static/file'
        fileid = len(os.listdir(folderurl)) + 1
        res = {'query_id':fileid,'query_content':query_content,'query_content_title':query_content_title}
        fileurl = folderurl + '/json' + str(fileid) + '.json'
        file_obj = open(fileurl,'w')
        json.dump(res,file_obj)
        file_obj.close()
        Record.objects.create(userid=user_id,dataurl=fileurl,time=datetime.datetime.now())
        return Response(res)
