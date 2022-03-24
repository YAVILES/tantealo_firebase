from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserDefaultSerializer
from rest_framework import status
from rest_framework.response import Response


class UserView(ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserDefaultSerializer


class NotificationView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    def post(self, request):
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
