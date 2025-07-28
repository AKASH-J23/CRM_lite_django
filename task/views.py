from django.shortcuts import render
from . import models
from .forms import TaskForm

def create_task(request, *args, **kwargs):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = models.Task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                due_date=form.cleaned_data['due_date'],
                assigned_to=form.cleaned_data['assigned_to'],
                status=form.cleaned_data['status'],
            )
            task.save()
            return render(request, 'task/detail.html', {'task': task})
    else:
        form = TaskForm()

    return render(request, 'task/create.html', {'form': form})

def list_tasks(request):
    tasks = models.Task.objects.all()
    return render(request, 'task/list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = models.Task.objects.get(pk=pk)
    return render(request, 'task/detail.html', {'task': task})

def task_update(request, pk):
    task = models.Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return render(request, 'task/detail.html', {'task': task})
    else:
        form = TaskForm(instance=task)

    return render(request, 'task/update.html', {'form': form, 'task': task})

def task_delete(request, pk):
    task = models.Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return render(request, 'task/list.html', {'tasks': models.Task.objects.all()})
    
    return render(request, 'task/delete.html', {'task': task})