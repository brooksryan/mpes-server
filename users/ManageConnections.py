import os

# Takes in an mpUserId and outputs a user object
from django.db import models
from .models import *

def getThisUsersAppId (mpUserId):
    
    thisUserId, created = MpUserProfile.objects.get_or_create(user_id=mpUserId)
    
    return thisUserId

def areThesePeopleConnected(creatorMpUserId, connectionMpUserId):
    
    print("hello")
    
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
    

    
    