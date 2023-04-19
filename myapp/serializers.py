from rest_framework import serializers

from .models import Card , List , Board

class signupSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    name = serializers.CharField(required=True)

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
    