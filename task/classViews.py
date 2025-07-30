from django.views import View, generic
from . import models
from django.shortcuts import render, redirect
from .forms import TaskModelForm, ContactForm
# from django.forms import formset_factory

class TaskListView(View):
    def get(self, request):
        tasks = models.Task.objects.all()
        return render(request, 'task/list.html', {'tasks': tasks})
    
class TaskDetailView(generic.DetailView):
    model = models.Task
    template_name = 'task/detail.html'
    context_object_name = 'task'
    # queryset = model.objects.filter(pk = id)

    def get_queryset(self):
        print(self.request.path)
        # id_field = self.request.id
        # return models.Task.objects.get(id=id_field)
        return models.Task.objects.all()