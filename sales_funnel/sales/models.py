from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name
    

class Status(models.Model):
    title = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.title
    

class Task(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('task', args=[self.id])
    
    def __str__(self) -> str:
        return self.title
