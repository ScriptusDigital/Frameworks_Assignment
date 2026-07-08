
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render

from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})     


#Logic for Profile view page updating
@login_required
def profile(request):

    profile_obj, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile_obj)

        if user_form.is_valid() and profile.form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Your profile has been updated.")
            return redirect("profile")
    
    else: 
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile_obj)

        

    return render(request, 'users/profile.html',)