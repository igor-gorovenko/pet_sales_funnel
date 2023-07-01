from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Task, User, Status
from .forms import CreateTaskFormUser, CreateTaskFormAdmin

DEFAULT_STATUS_ID = 1

def index(request):
    tasks_list = Task.objects.all()

    if request.user.is_staff == True:
        status_new = Task.objects.filter(status_id=1)
        status_open = Task.objects.filter(status_id=2)
        status_close = Task.objects.filter(status_id=3)
    else:
        status_new = Task.objects.filter(status_id=1).filter(user_id=request.user.id)
        status_open = Task.objects.filter(status_id=2).filter(user_id=request.user.id)
        status_close = Task.objects.filter(status_id=3).filter(user_id=request.user.id)
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
        new_task.user = User(id=request.user.id)
        new_task.save()
        return HttpResponseRedirect("/")
    else:
        add_task = CreateTaskFormUser()
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
            if request.user.is_staff == True:
                task.status = Status.objects.get(id=request.POST.get('status'))
            task.save()
            return HttpResponseRedirect("/")
        else:
            if request.user.is_staff == True:
                edit_task = CreateTaskFormAdmin()
                return render(request, "sales/edit_task.html", {"edit_task": edit_task})
            else:
                edit_task = CreateTaskFormUser()
                return render(request, "sales/edit_task.html", {"edit_task": edit_task})
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")
    

def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")