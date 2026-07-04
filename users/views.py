from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')


def profile(request):
    return render(request, 'profile.html')