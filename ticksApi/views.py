from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import userTick, feedStatus

# <My stuff
from users.models import MpUserProfile, Connections

# Classes from the serializer
from ticksApi.ticksSerializer import mpUserProfileSerializer, connectionsSerializer

from ticksApi.getUserTicks import getThisStuff

@csrf_exempt
def mpesUser_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        profiles = MpUserProfile.objects.all()
        serializer = mpUserProfileSerializer(profiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        
        return HttpResponse("Yo")
        
def connections_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        serializer_context = {
            'request': request,
        }
        profiles = Connections.objects.all()
        serializer = connectionsSerializer(profiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        
        return HttpResponse("Yo")
        
# _-_-_-_-_-_-_-_-_-_-_-NEW SHIT_-_-_-_-_-_-_-_-_-_-_-_-_-

# GET THE FEED STATUS FOR A USER

# def getUserFeedStatus(thisUserObject, thisFeedStatus):
    
#     return thisUserObject.doINeedToBeUpdated()
    
    
# brooks = MpUserProfile.objects.get(user_id = 111978840)



# thisFeed = feedStatus.objects.get(tickFeedOwner = brooks)

# thisFeed.updateThisFeed()

# theseUsers = brooks.get_following()

# def updateThesePeoplesFeeds(listOfUserObjects):
    
#     print(listOfUserObjects)
    
#     for userObjectItem in listOfUserObjects:
        
#         getThisStuff(userObjectItem)
        
# updateThesePeoplesFeeds(theseUsers)
        

# _-_-_-_-_-_-_-_-_-_-_-END NEW SHIT_-_-_-_-_-_-_-_-_-_-_-_

# Create your views here.
