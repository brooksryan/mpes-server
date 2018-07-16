# Takes in an mpUserId and outputs a user object
from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator

from .models import *
import ticksApi

def getThisUsersAppId (mpUserId):
    
    thisUserId, created = MpUserProfile.objects.get_or_create(user_id=mpUserId)
    
    return thisUserId

def areThesePeopleConnected(creatorMpUserId, connectionMpUserId):
    
    creatorIdToFind = getThisUsersAppId(creatorMpUserId)
    
    connectionIdToFind = getThisUsersAppId(connectionMpUserId)
    
    try:
    
        Connections.objects.get(creator = creatorIdToFind, following = connectionIdToFind)
        
    except:
        
        return False
        
    else:
        
        return True
    
def getOrCreateANewConnection (creatorUserId, newConnectionUserId):
    
    thisConnection, created = Connections.objects.get_or_create(creator = creatorUserId, following = newConnectionUserId)
    
    print(created)
    
    return thisConnection

    

def orchestrateANewConnection (creatorMpUserId,newConnectionMpUserId):
    
    newCreatorUserId = getThisUsersAppId(creatorMpUserId)
    
    newConnectionUserId = getThisUsersAppId(newConnectionMpUserId)
    
    thisConnectionInfo = getOrCreateANewConnection(newCreatorUserId, newConnectionUserId)
    
    return  thisConnectionInfo



def deleteAConnection (creatorUserId, newConnectionUserId): 
    
    connectionToDelete = Connections.objects.get(creator = creatorUserId, following = newConnectionUserId)
    
    return connectionToDelete.delete()
    
    
def orchestrateDeletingAConnection (creatorMpUserId,newConnectionMpUserId):
    
    CreatorUserIdToDelete = getThisUsersAppId(creatorMpUserId)
    
    ConnectionUserIdToDelete = getThisUsersAppId(newConnectionMpUserId)
    
    connectionToDelete = deleteAConnection(CreatorUserIdToDelete,ConnectionUserIdToDelete)
    
    return connectionToDelete
    
    
class FollowingTickFeed ():

    def __init__(self, mpUserId):
        
        self.mpUserId = mpUserId
    
    def myUserId(self):
        
        return getThisUsersAppId(self.mpUserId)
    
    def getMyFollowersTicks(self):
        
        theseUsers = []
    
        theseFollowers = self.myUserId().get_following()

        for item in theseFollowers:
            
            thisAppId = getThisUsersAppId(item.following)
            
            print(thisAppId.id)
            
            theseUsers.append(thisAppId.id)
            
        return ticksApi.models.userTick.objects.filter(creator__in=theseUsers).order_by('-date')
        
    def paginateFollowingTicks(self):
        
        thisPaginator = Paginator(self.getMyFollowersTicks(), 10)
        
        return(thisPaginator)
        
        
    def getTenMostRecentTicks(self, pageNum):
        
        return self.paginateFollowingTicks().page(pageNum).object_list
        
        
    
            
        

thisTickFeed = FollowingTickFeed(111978840)

thisPaginatedFeed = thisTickFeed.getTenMostRecentTicks(3)

print(thisPaginatedFeed)
    
    
            
            
            
            
            
# thisFeed = FollowingTickFeed(200105441)

# thisFeed.myUserId()

# thisFeed.getMyFollowersTicks()


    