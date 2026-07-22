
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from inbox.models import Message
from projects.models import Project
from django.utils import timezone

from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


#Dashboard fetches for projects and message displays
@login_required
def dashboard(request):

    user_projects = Project.objects.filter(owner=request.user)
    received_messages = Message.objects.filter(recipient=request.user)

    today = timezone.now().date()

    next_project = (
        user_projects
        .filter(end_date__isnull=False)
        .order_by("end_date")
        .first()
    )

    overdue_projects = (
        user_projects.filter(
            end_date__isnull=False,
            end_date__lt=today
        )

        .exclude(status="completed")
        .order_by("end_date")
    )

    context = {
        "total_projects": user_projects.count(),
        "active_projects": user_projects.filter(status="active").count(),
        "unread_messages": received_messages.filter(is_read=False, is_archived=False).count(),
        "archived_messages": received_messages.filter(is_archived=True).count(),
        "next_project": next_project,
        "overdue_projects": overdue_projects,
    }


    return render(request, 'dashboard.html',context)


#User creation logic 

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

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Your profile has been updated.")
            return redirect("profile")
    
    else: 
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile_obj)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }


    return render(request, 'users/profile.html', context)