from django.shortcuts import render
from . import models
from django.forms import Form

# def get_all_tasks_view(request):
#     content = ''
#     template_name = ''
#     if (request.method == 'GET'):
#         content = models.Task.objects.all()
#         template_name = 'task/list.html'

#     # if (request.method == 'POST'):
#     #     content = models.Task.create(
#     #         title=request.POST.get('title'),
#     #         description=request.POST.get('description'),
#     #         created_at=request.POST.get('created_at'),
#     #         due_date=request.POST.get('due_date'),
#     #         assigned_to=request.POST.get('assigned_to'),
#     #         updated_at=request.POST.get('updated_at'),
#     #         status=request.POST.get('status'),
#     #         created_by=request.POST.get('created_by')
#     #     )
#     #     template_name = 'task/list.html'

#     print("This is the content data", content)
    
#     context = {
#         'tasks': content
#     }
    
#     return render(request, template_name, context)

# def create_task_view(request):
    
#     context = {}
#     if (request.method == 'POST'):
#         content = Form(
#             title=request.POST.get('title'),
#             description=request.POST.get('description'),
#             created_at=request.POST.get('created_at'),
#             due_date=request.POST.get('due_date'),
#             assigned_to=request.POST.get('assigned_to'),
#             updated_at=request.POST.get('updated_at'),
#             status=request.POST.get('status'),
#             created_by=request.POST.get('created_by')
#         )
#         context['content'] = content

#     return render(request, 'task/create.html', context)