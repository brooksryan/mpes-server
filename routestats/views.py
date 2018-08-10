from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from . import getRouteStats

def getThisRouteStats(request):
    
    thisClimbToGetStatsFor = request.GET.get('url')
    
    # print(request.url)
    
    thisTickStats = getRouteStats.RouteStatHelper(thisClimbToGetStatsFor)
    
    data = {
        
        'averageNumberOfTicksPerGradeBeforeSend': thisTickStats.tickDictionary,
        
        'topFiveAtGradeBeforeTick': thisTickStats.topFiveMostFrequentAtThisGradeBeforeTick,
        
        'allTicksAtGradeBeforeTick': thisTickStats.ticksAtThisGradeDictionary
        
    }
    
    return JsonResponse(data, safe = False)
    
    # return JsonResponse("thisTickStats.tickDictionary", false)
    
    

# Create your views here.
