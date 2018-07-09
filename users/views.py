import os

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

# Import file for connection management
from . import ManageConnections

def index(request):
    
    return HttpResponse("stringdata")
    
    
def getThisUsersId(request,userMpId):
    
    thisUserId = ManageConnections.getThisUsersAppId(userMpId)
    
    return HttpResponse(thisUserId)

# def MakeANewConnection(request, userMpId, newConnectionMpId):
    
def createANewConnection(request, creatorMpId, connectionMpId):

    print("first call")
    thisNewConnection = ManageConnections.orchestrateANewConnection(creatorMpId, connectionMpId)
    
    print("print results")
    print (thisNewConnection.creator)
    print (" followed ") 
    print (thisNewConnection.following)
    
    return HttpResponse(thisNewConnection)
    
def checkThisConnection (request, creatorMpUserId, connectionMpUserId):

    connectionStatus = ManageConnections.areThesePeopleConnected(creatorMpUserId, connectionMpUserId)
    
    return HttpResponse(connectionStatus)