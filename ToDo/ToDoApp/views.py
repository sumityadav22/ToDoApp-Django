from django.shortcuts import redirect, render
from .forms import ToDoForm
from .models import ToDoModel

# Create your views here
def home(request):
    context = {
        'form': ToDoForm,
        'todo_item':ToDoModel.objects.all()
        }
    return render(request,"ToDo/index.html",context)

def addToDo(request):
    form_ob = ToDoForm(request.POST)
    if form_ob.is_valid():
        form_ob.save()
    return redirect('home')

def deleteToDo(request, todo_id):
    ToDoModel.objects.get(id = todo_id).delete()
    return redirect('home')