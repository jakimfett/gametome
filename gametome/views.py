from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile.html', {})

def game_view(request):
    return render(request, 'games.html', {})

def index_view(request):
    return render(request, 'index.html', {})
