from django.shortcuts import render
from rest_framework import permissions
from rest_framework import views
from .models import CustomUser
from .serializers import RegisterSerializer,UserListSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"register":201},status=status.HTTP_201_CREATED)
        else:
            return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class UserListApiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        users = CustomUser.objects.filter(~Q(id=request.user.id))
        return Response(UserListSerializer(users,many=True).data,status=status.HTTP_200_OK)

class UserInfoApiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,id):
        user = CustomUser.objects.get(id=id)
        return Response(UserListSerializer(user).data,status=status.HTTP_200_OK)


          