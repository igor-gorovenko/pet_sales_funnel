from django.contrib import admin
from .models import Task, Status, User


admin.site.register(Task)
admin.site.register(Status)
admin.site.register(User)
