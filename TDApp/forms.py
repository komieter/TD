from django import forms  
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        task = forms.CharField()
        fields = [
            'task',
            'completed',
        ]