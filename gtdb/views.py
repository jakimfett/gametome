from django.shortcuts import render
from models import *

# Create your views here.

def games(request):
    return render(request, 'games.html', {})

def index(request):
    ct = ContentType.objects.get(model='news')
    news_list = News.objects.filter(content_type=ct).order_by('-created_date').prefetch_related('comments')
    return render(request, 'index.html', {
        'news_list': news_list[:20],
    })
