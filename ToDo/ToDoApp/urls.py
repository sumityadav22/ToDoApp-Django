from django.urls import path
from .views import addToDo, deleteToDo, home, speak

urlpatterns = [
    path('',home,name = 'home'),
    path('add_todo/',addToDo,name = 'add_todo'),
    path('delete_todo/<int:todo_id>/',deleteToDo,name = 'delete_todo'),
    path('speak/<int:todo_id>/',speak,name = 'speak'),
]