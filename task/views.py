from django.shortcuts import render, redirect
from . import models
from .forms import TaskForm, TaskModelForm, ContactForm
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # task = models.Task(
            #     title=form.cleaned_data['title'],
            #     description=form.cleaned_data['description'],
            #     due_date=form.cleaned_data['due_date'],
            #     assigned_to=form.cleaned_data['assigned_to'],
            #     status=form.cleaned_data['status'],
            # )
            task.save()
            return redirect('tasks:task-detail', pk=task.pk)
            # return render(request, 'task/detail.html', {'task': task})
        else:
            print(form.errors)
    else:
        form = TaskModelForm()

    return render(request, 'task/create.html', {'form': form})

@login_required
def list_tasks(request):
    tasks = models.Task.objects.all()
    return render(request, 'task/list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = models.Task.objects.get(pk=pk)
    return render(request, 'task/detail.html', {'task': task})

@login_required
def task_update(request, pk):
    task = models.Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False) 
            updated_task.save()
            return redirect('tasks:task-detail', pk=updated_task.pk)
            # return render(request, 'task/detail.html', {'task': task})
    else:
        form = TaskModelForm(instance=task)

    return render(request, 'task/update.html', {'form': form, 'task': task})

@login_required
def task_delete(request, pk):
    task = models.Task.objects.get(pk=pk)
    print("task to delete", task)
    if request.method == 'POST':
        print("deleting task", task)
        task.delete()
        return redirect('tasks:task-list')
        # return render(request, 'task/list.html', {'tasks': models.Task.objects.all()})
    
    return render(request, 'task/delete.html', {'task': task})

ContactFormSet = formset_factory(ContactForm, extra=3)

@login_required
def formview(request):
    formset = ContactFormSet()
    return render(request, 'task/formset.html', {'formset': formset})
