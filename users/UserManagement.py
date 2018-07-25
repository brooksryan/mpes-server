from django.db import models
from django.core.exceptions import ObjectDoesNotExist

import requests, json

from .models import MpUserProfile

from ticksApi.getUserTicks import getThisStuff


def makeAUserRequestToMp(typeOfRequest,requestId):
    
    thisUrl = "https://www.mountainproject.com/data"
    
    myApiKey = "111978840-716a82f6d5cf048db82b3fdfdb6737be"
    
    if typeOfRequest == "user":
        
        thisPayload = {"userId": requestId, "key": myApiKey}
        
        userRequestUrl = thisUrl + "/get-user"
        
        thisRequest = requests.get(userRequestUrl, params = thisPayload)
        
        return thisRequest.text
    
    else:
        
        return "no other request type (shrug.ascii)"
        

class createNewUserHelper ():
    
    def __init__(self, mpUserId):
        
        # ACCEPTS A STRING YOU IDIOT
        self.mpUserId = mpUserId 
        
        self.userCsvUrl = 'https://www.mountainproject.com/user/' + str(mpUserId) + '/tick-export'
        
        self.thisUserModel = MpUserProfile()

    def getThisUsersMpUserName(self):
        
        thisUserContent = makeAUserRequestToMp("user", self.mpUserId)
        
        print(thisUserContent)
        
        thisUsersMpName = json.loads(thisUserContent)
        
        return thisUsersMpName
    
    def isThisAnExistingUser(self):
        
        try:
            
            thisUser = MpUserProfile.objects.get(user_id = self.mpUserId)
            
            print("this is a user")
            
            # print(thisUser.export_url)
            
            self.userCsvUrl = thisUser.export_url
            
            # getThisStuff(self.userCsvUrl, self.mpUserId)
            
            print(thisUser)
            
            return thisUser
        
        except ObjectDoesNotExist:
            
            print("Nothing here")
            
            return False
            
    def createAndSaveANewUser(self):
        
        if self.isThisAnExistingUser() == False:
        
            print("making a new user")
            
            self.thisUserModel.user_id = self.mpUserId
            
            thisUsersMpInfo = self.getThisUsersMpUserName()
            
            self.thisUserModel.name_from_mp = thisUsersMpInfo['name']
            
            self.thisUserModel.export_url = thisUsersMpInfo['url'] + '/tick-export'
            
            self.thisUserModel.save()
            
            # print(self.isThisAnExistingUser())
            
            return self.isThisAnExistingUser()
        
        else:
            
            return self.isThisAnExistingUser()
            
    # def getUserTicksIfTheyExist
                
        
        # create new user model
        # get user real name + mp data
        # get this users's ticks

# newPerson = createNewUserHelper(107529159)

# print(newPerson.createAndSaveANewUser().user_id)
    
    # create new user model
    # get user real name + mp data
    # get this users's ticks