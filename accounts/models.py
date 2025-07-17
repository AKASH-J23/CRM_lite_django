from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager

class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    EMPLOYEE = 'employee', 'Employee'
    MANAGER = 'manager', 'Manager'


# Create your models here.
class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email is required'), unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=30, choices=Role.choices, default=Role.EMPLOYEE)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.role}"

