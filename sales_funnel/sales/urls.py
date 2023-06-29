from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.get_task, name='task'),
    path('add_task/', views.add_task, name='add_task'),
]

