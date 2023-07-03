from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Status, User, Task

DEFAULT_STATUS_ID = 1


def index(request):
    if request.user.is_staff == True:
        status_new = Task.objects.filter(status_id=1)
        status_open = Task.objects.filter(status_id=2)
        status_close = Task.objects.filter(status_id=3)
    else:
        status_new = Task.objects.filter(status_id=1).filter(user_id=request.user.id)
        status_open = Task.objects.filter(status_id=2).filter(user_id=request.user.id)
        status_close = Task.objects.filter(status_id=3).filter(user_id=request.user.id)
    context = {
        'status_new': status_new,
        'status_open': status_open,
        'status_close': status_close,
    }
    return render(request, 'sales/index.html', context)


def get_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        'task': task,
    }
    return render(request, 'sales/detail_task.html', context)


def create_task(request):
    task = Task()
    status_list = Status.objects.all()

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.text = request.POST.get('text')
        task.user = User(id=request.user.id)
        if request.user.is_superuser == True:
            task.status = Status.objects.get(id=request.POST.get('status'))    
        else:
            task.status = Status(id=DEFAULT_STATUS_ID)
        task.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, 'sales/create_task.html', {
            'task': task,
            'status_list': status_list,
            })


def update_task(request, id):
    try:
        task = Task.objects.get(id=id)
        status_list = Status.objects.all()

        if request.method == "POST":
            task.title = request.POST.get('title')
            task.text = request.POST.get('text')
            if request.user.is_superuser == True:
                task.status = Status.objects.get(id=request.POST.get('status'))    
            task.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'sales/update_task.html', {
                'task': task,
                'status_list': status_list,
                })
    except Task.DoesNotExist:
        return HttpResponseNotFound('Task not found')
    

def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("Task not found")