# Takes in an mpUserId and outputs a user object
from django.db import models
from django.db.models import Q
from django.core.paginator import Paginator

# IMPORTS THE NEW USER HELPER
from .UserManagement import createNewUserHelper

# IMPORTS MODELS
from .models import MpUserProfile, Connections

from ticksApi.models import feedStatus


import ticksApi

def getThisUsersAppId (mpUserId):
    
    thisUser = createNewUserHelper(mpUserId)
    
    thisUserId = thisUser.createAndSaveANewUser()
    
    # thisUserId, created = MpUserProfile.objects.get_or_create(user_id=mpUserId)
    
    return thisUserId

def areThesePeopleConnected(creatorMpUserId, connectionMpUserId):
    
    creatorIdToFind = createNewUserHelper(creatorMpUserId)
    
    connectionIdToFind = createNewUserHelper(connectionMpUserId)
    
    try:
    
        Connections.objects.get(creator = creatorIdToFind.createAndSaveANewUser(), following = connectionIdToFind.createAndSaveANewUser())
        
    except:
        
        return False
        
    else:
        
        return True
    
def getOrCreateANewConnection (creatorUserId, newConnectionUserId):
    
    thisConnection, created = Connections.objects.get_or_create(creator = creatorUserId, following = newConnectionUserId)
    
    print(created)
    
    return created

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
        
        self.myUserId = getThisUsersAppId(mpUserId)
        
        self.thisFeedObject = feedStatus.objects.get(tickFeedOwner = self.myUserId)
    
    # input = appId output = all of the ticks from that users followers
    def getMyFollowersTicks(self):
        
        theseUsers = []
    
        theseFollowers = self.myUserId.get_following()
        
        print("this is after successfully returning followers from model")
        print (theseFollowers)

        for item in theseFollowers:
            
            print("this is the get my followers ticks iterator")
            print(item)
            
            thisAppId = item.following
            
            print(thisAppId.id)
            
            theseUsers.append(thisAppId.id)
            
        return ticksApi.models.userTick.objects.filter(creator__in=theseUsers).order_by('-date')
    
    # Input is getMyFollowersTicks (list of all this users following ticks)
    # Output is a paginated list of ticks
    def paginateFollowingTicks(self):
        
        thisPaginator = Paginator(self.getMyFollowersTicks(), 10)
        
        return(thisPaginator)
        
    # Input is a pageNumber and a paginated list of ticks
    # Output is the page of the paginated tick list per pageNumb
    def getTenMostRecentTicks(self, pageNum):
        
        self.thisFeedObject.doINeedToBeUpdated()
        
        if self.thisFeedObject.needsToBeUpdatedStatus == True:
            
            self.thisFeedObject.updateThisFeed()
        
            return self.paginateFollowingTicks().page(pageNum)
            
        else:
        
            return self.paginateFollowingTicks().page(pageNum)
        

    
    
            
            
            
            
            
# thisFeed = FollowingTickFeed(200105441)

# thisFeed.myUserId()

# thisFeed.getMyFollowersTicks()


    