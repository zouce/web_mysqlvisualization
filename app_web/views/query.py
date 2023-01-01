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
        '''
        query_res = Testtable.objects.raw(code)
        query_res = json.loads(serializers.serialize("json",query_res))
        query_content_title = []
        if len(query_res) > 0:
            for i in query_res[0]['fields']:
                query_content_title.append(i)
        query_content = []
        num = 1
        for i in query_res:
            item = i['fields']
            item['id'] = num
            num += 1
            query_content.append(item)
        #test = []
        #for i in list(query_res):
        #    test.append(list(i))
        #print(test)
        #for i in query_res:
        #    print("======")
        #    print(i,i.id,i.test)
        '''
        #query_content = [{'id':1,'col5':'11ds1','col2':'2fsf22','col3':'333'},{'id':2,'col5':'111','col2':'222','col3':'333'},{'id':3,'col5':'111','col2':'222','col3':'333'}]
        #query_content_title = ['col5','col2','col3']
        folderurl = '/home/zouce/web_mysqlvisualization/app_web/static/file'
        fileid = len(os.listdir(folderurl)) + 1
        res = {'query_id':fileid,'query_content':query_content,'query_content_title':query_content_title}
        
        fileurl = folderurl + '/json' + str(fileid) + '.json'
        file_obj = open(fileurl,'w')
        json.dump(res,file_obj)
        file_obj.close()
        Record.objects.create(userid=user_id,dataurl=fileurl,time=datetime.datetime.now())
        #df = pd.read_csv('~/HIGGS.csv.gz',header=None)
        #for i in range(4578029,11000000):
        #    HIGGS.objects.create(col1=df[0][i],col2=df[1][i],col3=df[2][i],col4=df[3][i],col5=df[4][i],col6=df[5][i],col7=df[6][i],col8=df[7][i],col9=df[8][i],col10=df[9][i],col11=df[10][i],col12=df[11][i],col13=df[12][i],col14=df[13][i],col15=df[14][i],col16=df[15][i],col17=df[16][i],col18=df[17][i],col19=df[18][i],col20=df[19][i],col21=df[20][i],col22=df[21][i],col23=df[22][i],col24=df[23][i],col25=df[24][i],col26=df[25][i],col27=df[26][i],col28=df[27][i],col29=df[28][i])
        
        return Response(res)
