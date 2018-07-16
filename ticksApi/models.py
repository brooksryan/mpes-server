from django.db import models

import uuid # Required for unique book instances

from users.models import MpUserProfile

class userTick(models.Model):
    
# MP tick data order 
# [Date,Route,Rating,Notes,URL,Pitches,Location,"Avg Stars","Your Stars",Style,"Lead Style","Route Type","Your Rating"]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this tick")
    
    # Date
    date = models.DateField()
    
    # Route
    route_name = models.CharField(max_length=100)
    
    # Rating
    difficulty = models.CharField(max_length=15)
    
    # Notes
    notes = models.CharField(max_length=300, blank=True, null=True)
    
    # URL
    route_url = models.CharField(max_length=300)
    
    # Calculate Route ID
    route_id = models.CharField(max_length=15)
    
    # Pitches
    pitches = models.IntegerField(default=1)
    
    # Location
    location = models.CharField(max_length=100)
    
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
    my_difficulty = models.CharField(max_length=15, blank=True, null=True)
    
    creator = models.ForeignKey(MpUserProfile, on_delete=models.CASCADE, related_name="tick_creator")
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.route_name

# Create your models here.
