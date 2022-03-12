from django.contrib import admin
from TodoApp import settings
from django.urls import (path , include)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include("todo.urls"))
]


if (settings.DEBUG):
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL)