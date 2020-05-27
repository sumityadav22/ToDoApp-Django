from django.shortcuts import render
from .forms import ToDoForm

# Create your views here
def Home(request):
    context = {
        'form': ToDoForm,
        }
    return render(request,"ToDo/index.html",context)