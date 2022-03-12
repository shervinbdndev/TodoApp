from django.shortcuts import (render , redirect)
from django.http import HttpResponse
from .models import TodoDatabase


def home(request):
    if (request.method == "POST"):
        title = request.POST.get("title")
        if (title is not None):
            TodoDatabase.objects.create(title = title)
        return redirect("home")

    data = TodoDatabase.objects.all()
    return render(request , "todo_temp/index.html" , {"data" : data})


def delete(request , id = None):
    data = TodoDatabase.objects.get(id = id)
    data.delete()
    return redirect("home")


def complete(request , id = None):
    data = TodoDatabase.objects.get(id = id)
    data.complete = True
    data.save()
    return redirect("home")