from django import forms
from .models import ToDoModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['text']
        
        widgets ={'text':forms.TextInput(attrs = {'class':'form-control','placeholder':'Type here...'})}