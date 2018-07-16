from django.db import models

from users.models import MpUserProfile, Connections

from .models import userTick

from rest_framework import serializers

class mpUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = MpUserProfile
        
        fields = ('user_id', 'id')
        
class connectionsSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Connections
        
        fields = ('created', 'creator', 'following')

