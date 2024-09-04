from django.shortcuts import render
from django.contrib.auth.decorators import login_not_required


@login_not_required
def index(request):
    return render(request, 'index.html')


@login_not_required
def about(request):
    return render(request, 'about.html')


def profile(request):
    return render(request, 'profile.html')
