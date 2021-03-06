"""favor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home_view, var_view
from home.views import home_view_quote
#from quote.views import quote_view
from todo.views import todo_view, todo_view_progress, delete_todo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    
    path('quote/',home_view_quote),
    path('var/', var_view),
    path("todos/", todo_view, name="todos"),
    
    path('todos/in_progress', todo_view_progress, name="in_progress"),
    path('todos/<pk>/delete', delete_todo, name="todo_del")
]