from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Task, User, Status
from .forms import CreateTaskForm

DEFAULT_STATUS_ID = 1


def index(request):
    tasks_list = Task.objects.all()
    status_new = Task.objects.filter(status_id=1)
    status_open = Task.objects.filter(status_id=2)
    status_close = Task.objects.filter(status_id=3)
    context = {
        'tasks_list': tasks_list,
        'status_new': status_new,
        'status_open': status_open,
        'status_close': status_close,
    }
    return render(request, 'sales/index.html', context)


def get_task(request, id):
    task = get_object_or_404(Task, pk=id)
    context = {
        'task': task,
    }
    return render(request, 'sales/detail_task.html', context)


def add_task(request):
    if request.method == 'POST':
        new_task = Task()
        new_task.title = request.POST.get('title')
        new_task.text = request.POST.get('text')
        new_task.status = Status(id=DEFAULT_STATUS_ID)
        new_task.save()
        return HttpResponseRedirect("/")
    else:
        add_task = CreateTaskForm()
        context = {
            'add_task': add_task,
        }
        return render(request, 'sales/add_task.html', context)
    

def edit_task(request, id):
    try:
        task = Task.objects.get(id=id)

        if request.method == "POST":
            task.title = request.POST.get("title")
            task.text = request.POST.get('text')
            task.save()
            return HttpResponseRedirect("/")
        else:
            edit_task = CreateTaskForm()
            return render(request, "sales/edit_task.html", {"edit_task": edit_task})
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
    

def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")