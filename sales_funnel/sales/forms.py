from django import forms

class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=40)
    text = forms.CharField(max_length=40)
    status = forms.Select({'id': 1})
    user = forms.Select({'two': 2})
