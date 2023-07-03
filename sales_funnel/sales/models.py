from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Status(models.Model):
    title = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.title
    

class Task(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
