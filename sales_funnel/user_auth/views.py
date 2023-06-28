from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'user_auth/register.html', {'form': form})
