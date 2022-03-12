from django.urls.base import reverse
from django.shortcuts import (render , redirect)
from django.http.request import HttpRequest
from django.views.generic.base import View
from .models import TodoDatabase





class HomeView(View):
    def get(self , request : HttpRequest):
        data : TodoDatabase = TodoDatabase.objects.all()
        return render(request=request , template_name='todo_temp/index.html' , context={'data' : data , 'title' : 'Todo Application'})
    
    def post(self , request : HttpRequest):
        title = request.POST.get('title')
        data : TodoDatabase = TodoDatabase(request.POST or None)
        if (data is not None):
            TodoDatabase.objects.create(title = title)
        return redirect(to=reverse(viewname='home'))




class DeleteView(View):
    def get(self , request : HttpRequest , id = None):
        data : TodoDatabase = TodoDatabase.objects.get(id = id)
        data.delete()
        return redirect(to=reverse(viewname='home'))




class CompleteView(View):
    def get(self , request : HttpRequest , id = None):
        data : TodoDatabase = TodoDatabase.objects.get(id = id)
        data.completed = True
        data.save()
        return redirect(to=reverse(viewname='home'))