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
    
    def create(self, validated_data):
        try:
            cards_data = validated_data.pop('cards')
            info_list = List.objects.create(**validated_data)
            for card_data in cards_data:
                card_data['cards'] = info_list
                Card.objects.create(**card_data)
            return info_list
        except Exception as e:
            print(e)
        info_list = List.objects.create(**validated_data)
        return info_list
    class Meta:
        model = List
        fields = ["id","title","cards","board"]

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)
class InfoBoardSerializer(serializers.ModelSerializer):
    lists = InfoListSerializer(many=True, required=False, allow_null=True)
    
    def create(self, validated_data):
        try:
            lists_data = validated_data.pop('lists')
            info_board = Board.objects.create(**validated_data)
            for list_data in lists_data:
                list_data['board'] = info_board
                List.objects.create(**list_data)
            return info_board
        except Exception as e:
            print(e)
        info_board = Board.objects.create(**validated_data)
        return info_board
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
