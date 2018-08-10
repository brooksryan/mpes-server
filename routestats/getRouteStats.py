from django.db import models
from django.db.models import Avg, Max, Min

# For rounding ticks
import math, re

from statistics import median

from ticksApi.models import userTick

# class thisRoutesStatsHelper():
    
# Return all of the ticks users have completed before completing this route

# functions 


# All users ticks
#input = routeid output = list of ticks done before this route by each person

class RouteStatHelper():
    
    def __init__(self, baseQueryFieldInput):
        
        # route URL to search for ticks
        self.baseQueryFieldInput = baseQueryFieldInput
        
        # returns a list of ticks for the matching route url
        self.theseUsersOriginalTicks = list(userTick.objects.filter(route_url = self.baseQueryFieldInput))
        
        # returns a querySet object for ticks matching route url (makes filtering easier later)
        self.querySetOfOriginalTicks = userTick.objects.filter(route_url = self.baseQueryFieldInput)
        
        # Init array to put the lowest tick for the route for each user in
        self.lowestTickDateForUsers = []
        
        # Stores difficulty for route
        self.originalTickDifficulty = self.theseUsersOriginalTicks[0].difficulty
        
        # Array of arrays where each array is a list of ticks for a user 
        # to put all of the ticks users completed before their first tick of a route
        self.filteredTicksByDate = []
        
        # raw array of all ticks for users ticks users completed before their 
        # first tick of a route this is different from filteredTicksBydate because
        # it is not an array of arrays
        self.allTicks = []
        
        self.filterOriginalTicksForFirstSend()
        
        self.getAllTicksForUsersWhoHaveDoneThisRoute()
        
        self.parseTicksForNoUsers()
        
        # initializes dictionary for storing summaries of the number of ticks the
        # average user completed at each grade before ticking this route for
        # the first time
        self.tickDictionary = {}
        
        self.ticksAtThisGradeDictionary = {}
        
        self.topFiveMostFrequentAtThisGradeBeforeTick = []
        
        self.getRouteGradeSummary()
        
        self.getCountOfRoutesAtSameGrade()
        
        # self.getMedianNumberOfRoutesDoneAtThisGrade()
        
    # gets all of the ticks for users who have done this route and filters them
    # for only the ticks that were done before the first time that user ticked
    # the route
    # This function is called in __init__
    
    # Takes in a query set containing all ticks by users who have ticked a route
    # and outputs a list containing query objects where each object is the earlist
    # tick a user completed a route
    def filterOriginalTicksForFirstSend(self):
        
        print("I'm at filterOriginalTicksForFirstSend")
        
        # groups the list of ticks by user and gets the lowest date for 
        # each user, outputting it into a dict
        oneResultPerUser = self.querySetOfOriginalTicks.values("creator") \
            .annotate(min_date = Min("date"))
        
        # iterates through the oneResultPerUser dict and gets the tick query object 
        # that matches the creater and the date and url and outputs them to  
        # a list
        for item in oneResultPerUser:
            
            thisTickQuerySet = userTick.objects.get(creator = item["creator"], date = item["min_date"], route_url = self.baseQueryFieldInput)
            
            self.lowestTickDateForUsers.append(thisTickQuerySet)
            
        return(self.lowestTickDateForUsers)
    
    # Takes in a list containing query objects for the earliest send of a route
    # by each user. Returns a list of all of the routes all of the users completed
    # before sending the route in question
    def getAllTicksForUsersWhoHaveDoneThisRoute(self):
        
        print("I'm in getAllTicksForUsersWhoHaveDoneThisRoute")
        
        theseTicks = self.lowestTickDateForUsers
        
        for item in theseTicks:

            ticksFilteredForDate = userTick.objects.filter(creator=item.creator) \
                .filter(date__lt = item.date) \
                .filter(route_type = item.route_type)
            
            self.filteredTicksByDate.append(ticksFilteredForDate)
        
        print("done with getAllTicksForUsersWhoHaveDoneThisRoute")
        
        return self.filteredTicksByDate
    
    # Input is an array of arrays where the childern arrays are arrays of 
    # query objects for user ticks. 
        
    def parseTicksForNoUsers(self):
        
        print("I'm in parseTicksForNoUsers")
        
        for user in self.filteredTicksByDate:
            
            for tick in user:
                
                self.allTicks.append(tick)
                
        return self.allTicks
    
    #returns the average number of climbs at each grade people who have ticked
    #this climb have ticked. 
    def getRouteGradeSummary(self):
        
        print ("I'm in getRouteGradeSummary")
        
        for tick in self.allTicks:
            
            splitTickDifficulty = re.split('\s|[a-d]\/|\+|\-',tick.difficulty)
            
            Difficultykey = splitTickDifficulty[0]
            
            if Difficultykey in self.tickDictionary:
                
                self.tickDictionary[Difficultykey] += 1
                
            else:
                
                self.tickDictionary[Difficultykey] = 1
        
        for key, value in self.tickDictionary.items():
            
            oldValue = value
            
            numberOfUsers = len(self.lowestTickDateForUsers)
            
            self.tickDictionary[key] = math.floor(oldValue/numberOfUsers)
            
        print(self.tickDictionary)
        
    def getMedianCountOfClimbsAtEachGrade(self):
        
        print("I'm in get median grade")
            
        
    def getCountOfRoutesAtSameGrade(self):
        
        print("I'm in getAllTicksForUsersWhoHaveDoneThisRoute")
        
        for item in self.filteredTicksByDate:
            
            filteredByDifficulty = item.filter(difficulty__contains = self.originalTickDifficulty)
            
            listOfTicksFilteredByDifficulty = list(filteredByDifficulty)
            
            for tick in listOfTicksFilteredByDifficulty:
                
                routeKey = tick.route_name
                
                if routeKey in self.ticksAtThisGradeDictionary:
                    
                    self.ticksAtThisGradeDictionary[routeKey] +=1
                    
                else:
                    
                    self.ticksAtThisGradeDictionary[routeKey] = 1
        
        sortedDict = sorted(self.ticksAtThisGradeDictionary.items(), key=lambda x: x[1], reverse=True)
                    
        self.ticksAtThisGradeDictionary = sortedDict
        
        self.topFiveMostFrequentAtThisGradeBeforeTick = sortedDict[0:5]

        print(self.topFiveMostFrequentAtThisGradeBeforeTick)
        
    
    # TODO, GET MEDIAN NUMBER OF CLIMBS AT EACH GRADE
        
    # def getMedianNumberOfRoutesDoneAtThisGrade(self):
        
    #     print("I'm in getAllTicksForUsersWhoHaveDoneThisRoute")
        
    #     numberOfTicksArray = []
        
    #     for item in self.filteredTicksByDate:
            
    #         filteredByDifficulty = item.filter(difficulty__contains = "5.10a")
            
    #         numberOfTicks = len(filteredByDifficulty)
            
    #         numberOfTicksArray.append(numberOfTicks)
            
    #     print (median(numberOfTicksArray))
            
        


# thisRouteStats.getAllTicksForUsersWhoHaveDoneThisRoute()




# print(thisRouteStats.theseUsersOriginalTicks)

# print(type(thisRouteStats.filteredTicksByDate))



# input list of a users ticks before this route
#     output other routes where gradeOfRoute == GradeOfThisRoute users have completed before this route
#     output number of routes at each grade users have completed before this route


