from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from gtdb.models import *

@login_required
def profile_view(request):
    return render(request, 'profile.html', {})

def game_view(request):
    return render(request, 'games.html', {})

def index_view(request):
    ct = ContentType.objects.get(model='news')
    news_list = News.objects.filter(content_type=ct).order_by('-created_date')#.prefetch_related('comments')
    return render(request, 'index.html', {
        'news_list': news_list[:20],
    })
