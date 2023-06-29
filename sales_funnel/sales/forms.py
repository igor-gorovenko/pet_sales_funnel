from django import forms
from .models import Status, User

class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=40)
    text = forms.CharField(max_length=40)
    status = forms.ChoiceField(choices={})
    user = forms.ChoiceField(choices={})
