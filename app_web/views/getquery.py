from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class GetQuery(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self, request):
        query_content = [{'id':1,'col1':'111','col2':'222','col3':'333'},{'id':2,'col1':'111','col2':'222','col3':'333'},{'id':3,'col1':'111','col2':'222','col3':'333'}]
        query_content_title = ['col1','col2','col3']

        return Response({'query_content':query_content,'query_content_title':query_content_title})
