from django import forms
from .models import Status


class CreateTaskFormUser(forms.Form):
    title = forms.CharField(max_length=40)
    text = forms.CharField(max_length=40)


class CreateTaskFormAdmin(forms.Form):
    title = forms.CharField(max_length=40)
    text = forms.CharField(max_length=40)
    status = forms.ModelChoiceField(label='', queryset=Status.objects.all(), empty_label='Status')
