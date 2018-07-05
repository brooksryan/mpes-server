from django.contrib import admin
from .models import ClassicRouteList, ClassicRoute, Author

admin.site.register(ClassicRouteList)

admin.site.register(Author)

admin.site.register(ClassicRoute)


# Register your models here.
