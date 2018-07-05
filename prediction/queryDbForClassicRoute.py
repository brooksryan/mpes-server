from django.db import models
from .models import ClassicRouteList, ClassicRoute, Author

# # a_record = ClassicRoutes(route_id=105889511)

# # # Save the object into the database.
# # a_record.save()

# # print(a_record.id)

def FindAllAuthorRouteItems():
    
    a = Author.objects.get(pk=1)
   
    q = ClassicRouteList.objects.all()[:5]
    
    return(q, a)

def queryForRoute(searchedRouteId):
    
    a = ClassicRoute.objects.get(route_id=searchedRouteId)
    
    return(a)