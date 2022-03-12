from django.urls.conf import path
from . import views


urlpatterns = [
    path(route="" , view=views.HomeView.as_view() , name = "home") ,
    path(route="delete/<int:id>" , view=views.DeleteView.as_view() , name = "delete") ,
    path(route="complete/<int:id>" , view=views.CompleteView.as_view() , name = "complete")
]