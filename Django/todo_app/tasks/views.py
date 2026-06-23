from .models import Task
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class=TaskSerializer
    queryset=Task.objects.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name= 'registration/signup.html'
    success_url=reverse_lazy('login')

class TaskListView(LoginRequiredMixin,ListView):
    model= Task
    template_name='tasks/home.html'
    context_object_name= 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin,CreateView):
    model= Task
    fields= ['title','done']
    template_name='tasks/create_task.html'
    success_url= reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model= Task
    fields=['title','done']
    template_name='tasks/edit_task.html'
    context_object_name='task'
    success_url=reverse_lazy('home')

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    template_name='tasks/del_task.html'
    success_url=reverse_lazy('home')

