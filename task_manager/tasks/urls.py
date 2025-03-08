from django.urls import path
from . import views
from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path('', views.task_list,),
    path('', task_list, name='task_list'),
    path('task_create/', task_create, name='task_create'),
    path('task_update/<int:id>/', task_update, name='task_update'),
    path('task_delete/<int:id>/', task_delete, name='task_delete'),
]