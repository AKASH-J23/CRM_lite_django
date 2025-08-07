from django.views import View, generic
from . import models
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import TaskModelForm, ContactForm
# from django.forms import formset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = models.Task.objects.all()
        return render(request, 'task/list.html', {'tasks': tasks})
    
class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Task
    template_name = 'task/detail.html'
    context_object_name = 'task'
    # queryset = model.objects.filter(pk = id)

    def get_queryset(self):
        print(self.request.path)
        # id_field = self.request.id
        # return models.Task.objects.get(id=id_field)
        return models.Task.objects.all()
    
class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Task
    template_name = 'task/create.html'
    form_class = TaskModelForm
    # success_url = '/'

    def form_valid(self, form):
        print("form cleaned datatta",form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks:task-detail', kwargs={'pk': self.object.pk})
        # return super().get_success_url()
    

class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Task
    template_name = 'task/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:task-list')
    
    def delete(self, request, *args, **kwargs):
        print("deleting task", self.get_object())
        return super().delete(request, *args, **kwargs)
    
class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Task
    template_name = 'task/update.html'
    form_class = TaskModelForm
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:task-list')

    def update(self, request, *args, **kwargs):
        print("updating task", self.get_object())
        return super().update(request, *args, **kwargs)