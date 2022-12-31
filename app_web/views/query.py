from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from app_web.models import Testtable
from django.core import serializers
import json, time, os

class Query(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self, request):
        data = request.POST
        code = str(data['code[_value]'])
        code = code.lower()
        code = code.replace('testtable','app_web_testtable')
        if(code.find("limit") == -1):
            code = code + " limit 100"
        query_res = Testtable.objects.raw(code)
        query_res = json.loads(serializers.serialize("json",query_res))
        query_content_title = []
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
        query_content = [{'id':1,'col5':'11ds1','col2':'2fsf22','col3':'333'},{'id':2,'col5':'111','col2':'222','col3':'333'},{'id':3,'col5':'111','col2':'222','col3':'333'}]
        query_content_title = ['col5','col2','col3']
        res = {'query_id':4,'query_content':query_content,'query_content_title':query_content_title}
        folderurl = '/home/zouce/web_mysqlvisualization/app_web/static/file'
        fileid = len(os.listdir(folderurl)) + 1
        print(fileid)
        fileurl = folderurl + '/json' + str(fileid) + '.json'
        print(fileurl)
        #file_obj = open(fileurl,'w')
        #json.dump(res,file_obj)
        #file_obj.close()
        return Response(res)
