from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('<int:userMpId>/', views.getThisUsersId, name='getUserId'),
    
    path('createNewConnection/<int:creatorMpId>/<int:connectionMpId>/', views.createANewConnection, name='createANewConnection'),
    
    path('deleteConnection/<int:creatorMpId>/<int:connectionMpId>/', views.deleteThisConnection, name='deleteConnection'),
    
    path('status/<int:creatorMpUserId>/<int:connectionMpUserId>/', views.checkThisConnection, name='checkThisConnection'),
    
    path('tickFeed/<int:userMpId>/<int:pageNumber>/', views.getThisUsersFollowersTickFeed, name='tickFeed'),
    
]