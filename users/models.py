import os

from django.db import models
import uuid # Required for unique book instances

import ticksApi

class MpUserProfile(models.Model):
    
    user_id = models.CharField(max_length=20, help_text="the user Id goes here")
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular user")
        
    def get_followers(self):
        
        followers = Connections.objects.filter(following=self.id)
        
        return followers
        
    def get_following(self):
        
        theseFollowing = Connections.objects.filter(creator=self.id)
        
        for line in theseFollowing:
            
            print (line.following)
            
        thisList = list(theseFollowing)
    
        return(theseFollowing)
        
    def get_my_ticks(self):
        
        theseTicks = ticksApi.models.userTick.objects.filter(creator=self.id)
        
        print(len(theseTicks))
        
        for item in theseTicks:
            
            print(item.route_name)
        
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.user_id
        
    
        
class Connections(models.Model):
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    creator = models.ForeignKey(MpUserProfile, on_delete=models.CASCADE, related_name="friendship_creator_set")
    
    following = models.ForeignKey(MpUserProfile, on_delete=models.CASCADE, related_name="friend_set")
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.following
    
# Create your models here.