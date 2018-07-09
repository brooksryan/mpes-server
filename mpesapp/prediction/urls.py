from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
        
    path('view2/<int:userID>/<int:routeID>', views.getPredictions, name='userPrediction'),
    
    path('allAuthorsAndLists', views.isThisRouteAClassic, name='allAuthors'),
    
    path('allAuthorsAndLists/<int:requestedId>', views.searchForThisRoute, name='allAuthors'),
    
]
