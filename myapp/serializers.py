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
        fields = ["id","description","order"]


class InfoListSerializer(serializers.ModelSerializer):
    cards = InfoCardSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = List
        fields = ["id","name","cards"]

class InfoBoardSerializer(serializers.ModelSerializer):
    lists = InfoListSerializer(many=True, required=False, allow_null=True)
    class Meta:

        model = Board
        fields = ["id","name","lists","owner"]
