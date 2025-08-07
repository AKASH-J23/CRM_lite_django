from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserModel

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    class Meta:
        model = CustomUserModel
        fields = ['email']