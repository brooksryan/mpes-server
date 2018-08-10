from django.urls import path
from . import views


urlpatterns = [
    
    path('getStats/', views.getThisRouteStats, name='getRouteStats')

]