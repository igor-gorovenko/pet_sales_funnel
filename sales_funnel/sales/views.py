from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Task, User, Status
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
        new_task = Task()
        new_task.title = request.POST.get('title')
        new_task.text = request.POST.get('text')
        new_task.status = Status(id=1)
        new_task.user = User(id=1)
        new_task.save()
        return HttpResponseRedirect("/")
    else:
        create_form = CreateTaskForm()
        context = {
            'create_form': create_form,
        }
        return render(request, 'sales/create_task.html', context)