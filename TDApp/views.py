from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse 
from .forms import TaskForm
from django.contrib import messages

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    return render(request, 'TDApp/home.html', {'tasks':tasks}) # we pass on the task to home.html

def add(request):
    
    if request.method == "POST": #check whether the user is inputing info
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() #save
            messages.success(request, ('Task has been added successfully!'))
            return redirect('home')
    else:
        form = TaskForm()
        return render(request, 'TDApp/add.html', {'form':form,})
    

def cross_off(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    messages.success(request, ('Task has been completed!'))
    return redirect('home')


def uncross(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = False
    task.save()
    messages.success(request, ('Still working on the task!'))
    return redirect('home')

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Task has been deleted!'))
    return redirect('home')
