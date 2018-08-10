from django.db import models


import datetime
from django.utils import timezone

import uuid # Required for unique book instances

# Imports User Profile model
from users.models import MpUserProfile

# from .getUserTicks import getThisStuff

class userTick(models.Model):
    
# MP tick data order 
# [Date,Route,Rating,Notes,URL,Pitches,Location,"Avg Stars","Your Stars",Style,"Lead Style","Route Type","Your Rating"]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this tick")
    
    # Date
    date = models.DateField()
    
    # Route
    route_name = models.CharField(max_length=200)
    
    # Rating
    difficulty = models.CharField(max_length=500)
    
    # Notes
    notes = models.CharField(max_length=1000000, blank=True, null=True)
    
    # URL
    route_url = models.CharField(max_length=500)
    
    # Calculate Route ID
    route_id = models.CharField(max_length=500)
    
    # Pitches
    pitches = models.IntegerField(default=1)
    
    # Location
    location = models.CharField(max_length=300)
    
    partner = models.ForeignKey(MpUserProfile, on_delete=models.CASCADE, related_name="partners", blank=True, null=True)
    
    # "Avg Stars"
    public_rating = models.FloatField(blank=True, null=True)
    
    # "Your Stars"
    my_rating = models.FloatField(blank=True, null=True)
    
    # Style
    style = models.CharField(max_length=100, blank=True, null=True)
    
    #"Lead Style"
    lead_style = models.CharField(max_length=100, blank=True, null=True)
    
    # "Route Type",
    route_type = models.CharField(max_length=100, blank=True, null=True)
    
    # "Your Rating"
    my_difficulty = models.CharField(max_length=500, blank=True, null=True)
    
    #creator name from MP
    user_name_from_mp = models.CharField(max_length=100, blank=True, null=True)
    
    # creator mp ID
    creator = models.ForeignKey(MpUserProfile, on_delete=models.CASCADE, related_name="tick_creator")
    
    def __str__(self):
        
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        
        if self.route_name == None: 
            
            return "THIS ROUTE DOES NOT HAVE A NAME"
            
        return self.route_name


# Model to know when a user's feed has last been updated. This model determines
# If the users that the current user is following need to have their ticks updated 
class feedStatus(models.Model):
    
    tickFeedOwner = models.OneToOneField(MpUserProfile, on_delete=models.CASCADE, related_name="tick_feed_owner", null=False)
    
    lastUpdatedDate = models.DateTimeField(auto_now_add=True, editable=True)
    
    needsToBeUpdatedStatus = models.BooleanField(default = True)
    
    # NEED TO FIGURE OUT WHY THIS ISN'T WORKING
    list_display = ('lastUpdatedDate', 'needsToBeUpdatedStatus')
    
    def doINeedToBeUpdated(self):
        
        rightNow = datetime.datetime.now(tz=timezone.utc)
        
        print(rightNow, "<-- right now  ~~~this is the two variables~~~ last updated--> ",self.lastUpdatedDate)
        
        
        timeDifference = rightNow - self.lastUpdatedDate
        
        timeDifferenceInHours = timeDifference.total_seconds()/60/60
        
        if timeDifferenceInHours > 1:
            
            self.needsToBeUpdatedStatus = True
            self.save(update_fields=['needsToBeUpdatedStatus'])
            
        else: 
            
            self.needsToBeUpdatedStatus = False
            self.save(update_fields=['needsToBeUpdatedStatus'])
    
    # updates the feed based on the current user's following list
    def updateThisFeed(self):
        
        thisUsersFollowing = self.tickFeedOwner.get_following()
        
        for userObjectItem in thisUsersFollowing:
            
            # Imports get User stuff here to avoid circular import
            from .getUserTicks import getThisStuff
            
            getThisStuff(userObjectItem.following)
            
        self.lastUpdatedDate = datetime.datetime.now(tz=timezone.utc)
        
        self.save(update_fields=['lastUpdatedDate'])
    
    doINeedToBeUpdated.short_description = "Time Difference"
    
    def __str__(self):
        
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        
        if self.tickFeedOwner == None: 
            
            return "THIS ROUTE DOES NOT HAVE A NAME"
            
        return self.tickFeedOwner.name_from_mp
    
    # Function for checking the last updated date
    
    # # Function for if the status needs to be updated, triggering the following
    # users feeds to be updated
    
    
    
    

# Create your models here.
