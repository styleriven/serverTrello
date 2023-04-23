from django.http import Http404, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import  User
from .models import Card,List,Board
from utils.token import create_access_token,get_tokens_for_user
from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from .serializers import *
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.db.models import Q
# @require_POST
# @transaction.atomic
""" class login(APIView):

    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid JSON body"}, status=400)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({"detail": "Email not found "}, status=404)
        if not check_password(password , user.password):
            return JsonResponse({"detail": "Incorrect password "}, status=401)

        access_token = get_tokens_for_user(user)
        return JsonResponse({"msg": "Successfully authenticated", "access_token": access_token,"id":user.id}, status=200)
 """
class sign_up(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            username = data.get('username')

            print(password)
        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid JSON body"}, status=400)
        try:
            # check exist username or email ///
            user = User.objects.filter(Q(username=username)| Q(email=email))
            return JsonResponse({"msg": "Email or username already exists"}, status=400)
        except User.DoesNotExist:
            user = User.objects.create_user(email=email, password=password,first_name=first_name, username=username, last_name=last_name)
            user.save()
            return JsonResponse({"msg": "User created successfully"}, status=200)



class InfoCard(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Card.objects.all()
    serializer_class = InfoCardSerializer


class InfoBoard(viewsets.ModelViewSet):
    serializer_class = InfoBoardSerializer


    def get_queryset(self):
        # Lấy thông tin người dùng đã đăng nhập
        user = self.request.user
        # Lấy danh sách board của người dùng đó
        queryset = Board.objects.filter(owner=user.id)
        return queryset




class InfoList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = List.objects.all()
    serializer_class = InfoListSerializer



# Token service


