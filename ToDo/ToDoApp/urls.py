from django.urls import path
from .views import AddToDo, DeleteToDo, Home

urlpatterns = [
    path('',Home,name = 'home'),
    path('add_todo/',AddToDo,name = 'add_todo'),
    path('delete_todo/<int:todo_id>/',DeleteToDo,name = 'delete_todo'),
]