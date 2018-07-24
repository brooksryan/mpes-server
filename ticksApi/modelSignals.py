from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import MpUserProfile

from .models import feedStatus

# function for tracking new mpUserProfiles being created. If a new MpUserProfile 
# is created, this function creates a corresponding feedStatus object for tracking
# the last time that users feed was updated

@receiver(post_save, sender=MpUserProfile)
def createUserFeedModelWhenUserIsCreated (sender, instance, created, **kwargs):
    
    if created:
        
        print("I TRACKED THE CREATION OF THIS OBJECT")
        
        print(instance)
        
        feedStatus.objects.create(tickFeedOwner=instance)