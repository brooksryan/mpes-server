from django.db import models
import uuid # Required for unique book instances


class Author(models.Model):
    #Fields
    AuthorName = models.CharField(max_length=1000)
    
    def __str__(self):
        
        return self.AuthorName
        
    def get_absolute_url(self):

        return reverse('model-detail-view', args=[str(self.id)])

class ClassicRouteList(models.Model):
    #Fields
    
    RouteListName = models.TextField(max_length=1000)
    
    ListAuthor = models.ManyToManyField(Author, help_text='What Classic List Is This Route On?')
    
    def __str__(self):
        
        return self.RouteListName
    
    def get_absolute_url(self):

        return reverse('model-detail-view', args=[str(self.id)])
    

class ClassicRoute(models.Model):
    #Fields
    RouteName = models.CharField(max_length=500, help_text="add the route ID here", blank=True, null=True)
    
    route_id = models.CharField(max_length=20, help_text="add the route ID here")
    
    routeList = models.ManyToManyField(ClassicRouteList, help_text='What Classic List Is This Route On?')
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular route")
    
    def __str__(self):
        
        return self.route_id
        
    def get_absolute_url(self):

        return reverse('model-detail-view', args=[str(self.id)])
        
# Create your models hçere.
