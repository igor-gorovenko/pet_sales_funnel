from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id_task>', views.task, name='task'),
    path('create_task/', views.create_new_task, name='create_task'),
]

