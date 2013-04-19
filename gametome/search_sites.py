from django.utils.timezone import now
from django.contrib.contenttypes.models import ContentType
from haystack.indexes import *
import haystack
from gtdb import models

class NewsIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        ct = ContentType.objects.get(model='news')
        return models.News.objects.filter(content_type=ct, updated_date__lte=now())
haystack.site.register(models.News, NewsIndex)

class GameIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return models.Game.objects.filter(updated_date__lte=now())
haystack.site.register(models.Game, GameIndex)

class CompanyIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        ct = ContentType.objects.get(model='company')
        return models.Company.objects.filter(content_type=ct, updated_date__lte=now())
haystack.site.register(models.Company, CompanyIndex)

haystack.autodiscover()
