from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class GetInfo(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        return Response({'username': user.username})
