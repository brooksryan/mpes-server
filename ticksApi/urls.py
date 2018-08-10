from django.urls import path

from ticksApi import views

urlpatterns = [

   path('routeTickProcessor', views.importAllTicksForThisRoute, name='routeTickProcessor'),
    
]