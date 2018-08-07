from django.db import models
from django.db.models import Avg, Max, Min

from ticksApi.models import userTick

# class thisRoutesStatsHelper():
    
# Return all of the ticks users have completed before completing this route

# functions 


# All users ticks
#input = routeid output = list of ticks done before this route by each person

class RouteStatHelper():
    
    def __init__(self, baseQueryFieldInput):
        
        self.baseQueryFieldInput = baseQueryFieldInput
        
        self.theseUsersOriginalTicks = list(userTick.objects.filter(route_url = self.baseQueryFieldInput))
        
        self.querySetOfOriginalTicks = userTick.objects.filter(route_url = self.baseQueryFieldInput)
        
        self.lowestTickDateForUsers = []
        
        self.originalTickDifficulty = self.theseUsersOriginalTicks[0].difficulty
        
        self.filteredTicksByDate = []
        
        self.allTicks = []
        
        self.filterOriginalTicksForFirstSend()
        
        self.getAllTicksForUsersWhoHaveDoneThisRoute()
        
        self.parseTicksForNoUsers()
        
        self.tickDictionary = {}
        
        self.getRouteGradeSummary()
        
        self.filterOriginalTicksForFirstSend()
        
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
                .filter(route_type = item.route_type) \
                .filter(style = item.style)
            
            self.filteredTicksByDate.append(ticksFilteredForDate)
        
        print("done with getAllTicksForUsersWhoHaveDoneThisRoute")
        
        return self.filteredTicksByDate
        
    def parseTicksForNoUsers(self):
        
        print("I'm in parseTicksForNoUsers")
        
        for user in self.filteredTicksByDate:
            
            for tick in user:
                
                self.allTicks.append(tick)
                
        return self.allTicks
        
    def getRouteGradeSummary(self):
        
        print ("I'm in getRouteGradeSummary")
        
        for tick in self.allTicks:
            
            Difficultykey = tick.difficulty
            
            if Difficultykey in self.tickDictionary:
                
                self.tickDictionary[Difficultykey] += 1
                
            else:
                
                self.tickDictionary[Difficultykey] = 1
            
        
    def getCountOfRoutesAtSameGrade(self):
        
        print("I'm in getAllTicksForUsersWhoHaveDoneThisRoute")
        
        for item in self.filteredTicksByDate:
            
            filteredByDifficulty = item.filter(difficulty__contains = self.originalTickDifficulty)
            
            print(len(filteredByDifficulty))
            
            print(filteredByDifficulty)


thisRouteStats = RouteStatHelper("https://www.mountainproject.com/route/105812520/traveler-buttress")

# thisRouteStats.getAllTicksForUsersWhoHaveDoneThisRoute()

thisRouteStats.getCountOfRoutesAtSameGrade()

print(thisRouteStats.tickDictionary)




# print(thisRouteStats.theseUsersOriginalTicks)

# print(type(thisRouteStats.filteredTicksByDate))



# input list of a users ticks before this route
#     output other routes where gradeOfRoute == GradeOfThisRoute users have completed before this route
#     output number of routes at each grade users have completed before this route


