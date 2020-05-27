from django.urls import path
from .views import AddToDo, Home

urlpatterns = [
    path('',Home,name = 'home'),
    path('add_todo/',AddToDo,name = 'add_todo'),
]