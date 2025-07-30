app_name = 'tasks'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='task-list'),
    path('create/', views.create_task, name='task-create'),
    path('<int:pk>/', views.task_detail, name='task-detail'),
    path('<int:pk>/update/', views.task_update, name='task-update'),
    path('<int:pk>/delete/', views.task_delete, name='task-delete'),
    path('formset/', views.formview, name='formset-view'),
]