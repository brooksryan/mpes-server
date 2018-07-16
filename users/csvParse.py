import csv
import datetime
import time

# Import user profile and user tick models
from .models import MpUserProfile

# Import connection management functions
from . import ManageConnections


PATH = 'ticks.csv'

mpUserId = 111978840

# parse a tick csv
def mapTickToModel (listForTick, MpUserId):
    
        for line in listForTick:
        
            if line[0] == 'Date':
            
                print (line[0])
                
            else: 
        
                thisTick = userTick()
                
                thisTick.date = listForTick[0]
                
                createTickFromModel(line, MpUserId)
                        
                print(thisTick)


def createTickFromModel(thisList, MpUserId):
    
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
    
    print(thisTick())
    
    # "tick owner"
    
    # Partner
    
    # Calculate Route ID

# Open CSV with MPuserid
def readFile (thisCSV, mpUserId, functionToParse):
    
    thisMpUserId = mpUserId
    
    thisfile = open(thisCSV)
    
    print(thisfile)

    read = list(csv.reader(thisfile))
    
    functionToParse(read, thisMpUserId)
        

readFile(PATH,mpUserId,mapTickToModel)

    
# def createANewTick(csvLineList, userid):
    
# save the data to a tick for that user