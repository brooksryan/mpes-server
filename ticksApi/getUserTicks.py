# System Imports
import requests
import csv

from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Local model imports
from .models import userTick

# STUFF FROM USERS APP
# User profile model
from users.models import MpUserProfile
# function for getting the users mpes id from their MP id
# from users.ManageConnections import getThisUsersAppId
# from users.UserManagement import createNewUserHelper



def getOrCreateANewTickBasedOnDateAndUser (tickObject):
    
    # print(tickObject.creator)
    
    print(tickObject.date)
     
    # print(tickObject.route_url)
    
    try: 
        
        thisTick = userTick.objects.get(creator = tickObject.creator, date = tickObject.date, route_url = tickObject.route_url)
        
        print(thisTick)
        
        return(thisTick)
        
    except ObjectDoesNotExist:
    
        thisTick = "hello"
        
        savingThisTick = tickObject.save()
        
        return(savingThisTick)


def createTickFromModel(thisList, thisUserObject):
    
    print(thisList)
    
    thisTick = userTick()
    
    thisListNumber = 0
    
    thisTick.date = thisList[thisListNumber]
    
    thisListNumber += 1
    # Route
    thisTick.route_name = thisList[thisListNumber]
    
    thisListNumber += 1
    # Rating
    thisTick.difficulty = thisList[thisListNumber]
    
    thisListNumber += 1
    # Notes
    thisTick.notes = thisList[thisListNumber]
    
    thisListNumber += 1
    # URL
    thisTick.route_url = thisList[thisListNumber]
    
    thisListNumber += 1
    # Pitches
    thisTick.pitches = thisList[thisListNumber]
    
    thisListNumber += 1
    # Location
    thisTick.location = thisList[thisListNumber]
    
    thisListNumber += 1
    # "Avg Stars"
    thisTick.public_rating = thisList[thisListNumber]
    
    thisListNumber += 1
    # "Your Stars"
    thisTick.my_rating = thisList[thisListNumber]
    
    thisListNumber += 1
    # Style
    thisTick.style = thisList[thisListNumber]
    
    thisListNumber += 1
    #"Lead Style"
    thisTick.lead_style = thisList[thisListNumber]
    
    thisListNumber += 1
    # "Route Type",
    thisTick.route_type = thisList[thisListNumber]
    
    thisListNumber += 1
    # "Your Rating"
    thisTick.my_difficulty = thisList[thisListNumber]
    
    # print(MpUserId)
    
    thisTick.user_name_from_mp = thisUserObject.name_from_mp
    
    thisTick.creator = MpUserProfile.objects.get(user_id = thisUserObject.user_id)
    
    # print(thisTick())
    getOrCreateANewTickBasedOnDateAndUser (thisTick)

# def getThisStuff(thisCsvUrl, thisMpUserId):
    
def getThisStuff(userObject):
    
    # print (thisCsvUrl, thisMpUserId)
    
    # thisTickListUserAppId = getThisUsersAppId(thisMpUserId)

    r = requests.get(str(userObject.export_url))
    
    # thisNewFile = open(r.content)
    
    # print(thisNewFile)
    
    # decodedContent = r.content.decode('utf-8')
    
    thiscontent = r.text
    
    readThis = csv.reader(thiscontent.splitlines(), delimiter=',')
    
    print(readThis)
    
    lineNumber = 0
    
    for line in readThis:
        
        if line[0] == "Date":
            
                print ("caught you")
                
        else:
            
            print(lineNumber)
        
            lineNumber += 1
            
            amIANewTick = createTickFromModel(line, userObject)

    
    # getThisStuff('https://www.mountainproject.com/user/111816786/tick-export', 111816786)