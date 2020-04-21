from django.shortcuts import render
from .models import Todo

# Create your views here.
def todo_view(request):
    todos = Todo.objects.all()
    data = {
       "todos" : todos,
    }
    return render(request, "todo_list.html", data)

def todo_view_progress(request):
    todos = Todo.objects.all()
    data = {
       "todos": todos,
    }
    return render(request, "todo_list_yet.html", data)
