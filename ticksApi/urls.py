from django.conf.urls import url
from ticksApi import views

urlpatterns = [

    url(r'^connections/$', views.connections_list),
    
]