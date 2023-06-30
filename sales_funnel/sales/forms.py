from django import forms

class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=40)
    text = forms.CharField(max_length=40)