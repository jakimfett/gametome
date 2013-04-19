from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.contrib.contenttypes.models import ContentType
from haystack.indexes import *
from haystack import site
from django.utils.timezone import now
#from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation

# Create your models here.
@python_2_unicode_compatible
class Entity(models.Model):
    title = models.CharField(max_length=255)
    short = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)
    reporter = models.CharField(max_length=50, null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    
    tags = TaggableManager()

    def get_real(self):
        return self.content_type.model_class().objects.get(pk=self.pk)

    def save(self, *args, **kwargs):
        self.content_type = ContentType.objects.get_for_model(self, for_concrete_model=False)
        super(Entity, self).save(*args, **kwargs)  # Call the "real" save() method.

    def desc_short(self):
        if self.description:
            return (self.description[:48] + '..') if len(self.description) > 50 else self.description
        else:
            return ''
        
    def __str__(self):
        return self.title

    
class Relation(models.Model):
    a = models.ForeignKey(Entity, related_name='related_to')
    b = models.ForeignKey(Entity, related_name='related_from')
    type = models.CharField(max_length=50)

class URLlink(models.Model):
    entity = models.ForeignKey(Entity, related_name='urls')
    desc = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

class Comment(Entity):
    entity = models.ForeignKey(Entity, related_name='comments')
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

class News(Entity):
    class Meta:
        proxy = True
    
    def get_absolute_url(self):
        return "/news/%d/" % (self.pk)
class NewsIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        ct = ContentType.objects.get(model='news')
        return News.objects.filter(content_type=ct, updated_date__lte=now())
site.register(News, NewsIndex)

class Game(Entity):
    cost = models.CharField(max_length=255)
    version = models.CharField(max_length=255)

    def get_absolute_url(self):
        return "/games/%d/" % (self.pk)
class GameIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Game.objects.filter(updated_date__lte=now())
site.register(Game, GameIndex)

class Review(Entity):
    entity = models.ForeignKey(Entity, related_name='reviews')
    score = models.IntegerField()

class Company(Entity):
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return "/company/%d/" % (self.pk)
class CompanyIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        ct = ContentType.objects.get(model='company')
        return Company.objects.filter(content_type=ct, updated_date__lte=now())
site.register(Company, CompanyIndex)

    