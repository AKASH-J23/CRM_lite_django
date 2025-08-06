app_name = 'tasks'
from django.urls import path
from . import views
from .classViews import TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('formset/', views.formview, name='formset-view'),
]