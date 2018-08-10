# given a bunch of user Ids from mountain project, download all of their ticks
from users.ManageConnections import getThisUsersAppId

from ticksApi.getUserTicks import getThisStuff

def getAllUserTicksForThisRoute(arrayOfUserIds):
    
    for userId in arrayOfUserIds:
        
        thisUsersAppId = getThisUsersAppId(userId)
        
        getThisStuff(thisUsersAppId)