
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from .forms import UserRegisterForm

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})     


@login_required
def profile(request):
    return render(request, 'users/profile.html')