import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db import models

# REST stuff
from rest_framework import viewsets

# Import file for connection management
from . import ManageConnections, UserManagement

from ticksApi.getUserTicks import getThisStuff

# import models
from .models import MpUserProfile, Connections

def index(request):
    
    return HttpResponse("stringdata")
    
    
def getThisUsersId(request,userMpId):
    
    thisUserId = ManageConnections.getThisUsersAppId(userMpId)
    
    return HttpResponse(thisUserId)

# def MakeANewConnection(request, userMpId, newConnectionMpId):
    
def createANewConnection(request, creatorMpId, connectionMpId):
    thisNewConnection = ManageConnections.orchestrateANewConnection(creatorMpId, connectionMpId)
    
    newConnectionTicksToGet = ManageConnections.getThisUsersAppId(connectionMpId)
    
    print (newConnectionTicksToGet.export_url)
    
    getThisStuff(newConnectionTicksToGet)
    
    # print("print results")
    # print (thisNewConnection.creator)
    # print (" followed ") 
    # print (thisNewConnection.following)
    
    return HttpResponse(thisNewConnection)
    
def checkThisConnection (request, creatorMpUserId, connectionMpUserId):

    connectionStatus = ManageConnections.areThesePeopleConnected(creatorMpUserId, connectionMpUserId)
    
    return HttpResponse(connectionStatus)
    
def deleteThisConnection (request, creatorMpId, connectionMpId):
    
    connectionDeleted = ManageConnections.orchestrateDeletingAConnection(creatorMpId, connectionMpId)
    
    return HttpResponse(connectionDeleted)
    
def getThisUsersFollowersTickFeed(request, userMpId, pageNumber):
    
    thisUserFeed = ManageConnections.FollowingTickFeed(userMpId)
    
    # thisUserFeed.thisFeedObject.updateThisFeed()
    
    theseRecentTicksPageObject = thisUserFeed.getTenMostRecentTicks(pageNumber)
    
    theseRecentTicks = theseRecentTicksPageObject.object_list
    
    serializedData = serializers.serialize('json', list(theseRecentTicks))
    
    nextPage = pageNumber + 1
    
    hasNextPage = theseRecentTicksPageObject.has_next()
    
    hasPreviousPage = theseRecentTicksPageObject.has_previous()
    
    thisFeedData = {
        
        'feedItems' : serializedData,
        
        'currentPage' : pageNumber,
        
        'nextPage': nextPage,
        
        'hasNextPage': hasNextPage,
        
        'hasPreviousPage': hasPreviousPage
        
    }
    
    return JsonResponse(thisFeedData, safe=False)
    
    



# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#       'users': reverse('users:user-list', request=request, format=format),
#       'todos': reverse('todos:todo-list', request=request, format=format),
#     })
