from django.contrib import admin
from TodoApp import settings
from django.conf.urls.static import static
from django.urls.conf import (path , include)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path(route='admin/', view=admin.site.urls , name='admin'),
    path(route='' , view=include("todo.urls") , name='index') 
]


if (settings.DEBUG):
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL)