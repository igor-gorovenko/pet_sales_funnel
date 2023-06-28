from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import CreateTaskForm


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
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        return HttpResponse(f"Заголовок {title} описание {text}")
    else:
        create_form = CreateTaskForm()
        context = {
            'create_form': create_form,
        }
        return render(request, 'sales/create_task.html', context)
