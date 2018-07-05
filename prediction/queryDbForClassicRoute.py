from django.db import models
from .models import ClassicRouteList, ClassicRoute, Author
from django.core import serializers

from django.shortcuts import get_object_or_404

# # a_record = ClassicRoutes(route_id=105889511)

# # # Save the object into the database.
# # a_record.save()

# # print(a_record.id)

def FindAllAuthorRouteItems():
    
    a = Author.objects.get(pk=1)
   
    q = ClassicRouteList.objects.all()[:5]
    
    return(q, a)
    
    
# SEARCHES FOR A ROUTE ID AND RETURNS THE CLASSIC LISTS
# THAT ROUTE APPEARS ON IF ANY
def queryForRoute(searchedRouteId):
    
    try:
    
        a = get_object_or_404(ClassicRoute, route_id=searchedRouteId)
        
    except ClassicRoute.DoesNotExist:
        
        return("Couldn't find that thing")
    
    else:
        
        data = serializers.serialize("json", a.routeList.all()) 
        
        return (data)
    
    


    # if a 
    
    #     thisResponse = serializers.serialize("json", a.routeList.all()) 
    
    #     return(thisResponse)
        
    # else 
    
    #     thisResponse = "that record does not exist"
        
    #     return(thisResponse)