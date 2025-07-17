from django.db import models
from django.utils import timezone
from datetime import timedelta

def calculate_due_date():
    return timezone.now() + timedelta(hours=2)

choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True, default=calculate_due_date)
    assigned_to = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=choices, default='pending')
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title