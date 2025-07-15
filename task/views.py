from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django import shortcuts


def first_view(request):
    print(dir(shortcuts))
    return HttpResponse("Hello, world. You're at the task index.")
# Create your views here.

def second_view(request):
    data = {
        'message': 'This is the second view.',
        'status': 'success'
    }
    return JsonResponse(data)
