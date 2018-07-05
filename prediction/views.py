import os

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from . import surprisePredictions, queryDbForClassicRoute

def index(request):
    
    return HttpResponse("stringdata")
    
def getPredictions (request, userID, routeID):
    
    thisPrediction = "placeholder because I don't want to retrain"
    
    # thisPrediction = surprisePredictions.getThisUsersPredictions(userID, routeID)
    
    return HttpResponse(thisPrediction)
    
def isThisRouteAClassic(request):
    
    AllAuthorAndListItems = queryDbForClassicRoute.FindAllAuthorRouteItems()
    
    print (type(AllAuthorAndListItems[1]))
    
    print(AllAuthorAndListItems)

    return HttpResponse(AllAuthorAndListItems[1])
    
def searchForThisRoute(request,requestedId):
    
    AllAuthorAndListItems = queryDbForClassicRoute.queryForRoute(requestedId)
    
    print (type(AllAuthorAndListItems))
    
    print(AllAuthorAndListItems)

    return HttpResponse(AllAuthorAndListItems.routeList.all())
    
    
# Create your views here.