from django import forms
from django.utils.translation import gettext_lazy as _
import re
from .models import Task

choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to', 'status']
        widgets = {
            'due_date': forms.SelectDateWidget(),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if not re.match(r"^[a-zA-Z\s]+$", title):
            raise forms.ValidationError(_("Title must contain only letters and spaces."))
        if len(title.strip()) == 0:
            raise forms.ValidationError(_("Title cannot be empty."))
        return title

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    

class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, label=_("Title"), required=True)
    description = forms.CharField(widget=forms.Textarea, label=_("Description"), required=False)
    due_date = forms.DateField(label=_("Due Date"), widget=forms.SelectDateWidget(), required=False)
    assigned_to = forms.CharField(max_length=100, label=_("Assigned To"), required=False)
    status = forms.ChoiceField(choices=choices, label=_("Status"), initial='pending', required=True)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not re.match(r"^[a-zA-Z\s]+$", title):
            raise forms.ValidationError(_("Title must contain only letters and spaces."))
        if len(title.strip()) == 0:
            raise forms.validationError(_("Title cannot be empty."))
        return title