from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'completed']

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'completed']

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
