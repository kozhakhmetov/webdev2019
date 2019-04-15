from django.contrib import admin
from django.urls import path, include

from api import views


from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('task_lists', csrf_exempt(views.TaskLists.as_view())),
    path('task_lists/<int:id>', csrf_exempt(views.TaskList.as_view())),
    path('task_lists/<int:id>/tasks', csrf_exempt(views.TasksById.as_view()))
]
