from rest_framework import serializers

from .models import Card , List , Board
from django.contrib.auth.models import  User
class signupSerializer(serializers.Serializer):
     class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'username')

class InfoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id","description","order", "title","list"]


class InfoListSerializer(serializers.ModelSerializer):
    cards = InfoCardSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = List
        fields = ["id","title","cards","board"]

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)
class InfoBoardSerializer(serializers.ModelSerializer):
    lists = InfoListSerializer(many=True, required=False, allow_null=True)
    class Meta:

        model = Board
        fields = ["id","name","lists","owner"]
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['user_id'] = self.user.id
        return data
