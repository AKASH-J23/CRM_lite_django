from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('a/', views.second_view, name='second_view'),
]