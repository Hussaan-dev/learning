from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model= Task
    template_name='tasks/home.html'
    context_object_name= 'tasks'

class TaskCreateView(CreateView):
    model= Task
    fields= ['title','done']
    template_name='tasks/create_task.html'
    success_url= reverse_lazy('home')

class TaskUpdateView(UpdateView):
    model= Task
    fields=['title','done']
    template_name='tasks/edit_task.html'
    context_object_name='task'
    success_url=reverse_lazy('home')

class TaskDeleteView(DeleteView):
    model=Task
    template_name='tasks/del_task.html'
    success_url=reverse_lazy('home')

