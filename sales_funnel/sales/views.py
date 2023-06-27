from django.shortcuts import render, get_object_or_404
from .models import Task


def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list,
    }
    return render(request, 'sales/index.html', context)


def task(request, id_task):
    task = get_object_or_404(Task, id=id_task)
    context = {
        'task': task,
    }
    return render(request, 'sales/detail_task.html', context)
