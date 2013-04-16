from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    ct = ContentType.objects.get(model='news')
    news_list = News.objects.filter(content_type=ct).order_by('-created_date').prefetch_related('comments')
    return render(request, 'index.html', {
        'news_list': news_list[:20],
    })

def news(request, news_id):
    return render(request, 'news_item.html', {
        'news': News.objects.get(pk=news_id)
    })

def games(request):
    games_list = Game.objects.all().order_by('-created_date').prefetch_related('comments')
    return render(request, 'games.html', {
        'games_list': games_list[:20],
    })

def game(request, game_id):
    return render(request, 'game_item.html', {
        'game': Game.objects.get(pk=game_id)
    })
