from django.shortcuts import render, get_object_or_404
from .models import Task


def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list,
    }
    return render(request, 'sales/index.html', context)


def task(request, id):
    task = get_object_or_404(Task, pk=id)
    context = {
        'task': task,
    }
    return render(request, 'sales/detail_task.html', context)


def create_new_task(request):
    new_task = 'test'
    context = {
        'new_task': new_task,
    }
    return render(request, 'sales/create_task.html', context)
