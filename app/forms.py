from django import forms
from django.forms import DateTimeInput

from app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "user",
            "header",
            "content",
            "deadline",
            "done_or_not",
        ]
        exclude = ("user",)
        widgets = {
            "deadline": DateTimeInput(attrs={"placeholder": "Enter deadline like: 2022-12-25"}),
        }
