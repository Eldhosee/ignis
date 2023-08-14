from rest_framework import serializers
from .models import User,Events,Likes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)
class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'