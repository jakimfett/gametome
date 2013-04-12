from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.contrib.contenttypes.models import ContentType
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

class News(Entity):
    class Meta:
        proxy = True

class Game(Entity):
    cost = models.CharField(max_length=255)
    version = models.CharField(max_length=255)

class Review(Entity):
    entity = models.ForeignKey(Entity, related_name='reviews')
    score = models.IntegerField()

class Company(Entity):
    class Meta:
        proxy = True

'''
@python_2_unicode_compatible
class Log(models.Model):
    # GenericForeignKey
    object_id = models.IntegerField(verbose_name='Object id', db_index=True)
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Content type',
        related_name="%(app_label)s_%(class)s_logs"
    )
    content_object = GenericForeignKey()
    #content_object.verbose_name='Entity'

    date = models.DateTimeField(auto_now_add=True, blank=True)
    log = models.TextField()
    
    def log_short(self):
        return (self.log[:48] + '..') if len(self.log) > 50 else self.log
    
    def __str__(self):
        return self.log_short()

@python_2_unicode_compatible
class Entity(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)
    
    tags = TaggableManager()
    logs = GenericRelation(Log)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class News(Entity):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.CharField(max_length=50)#models.ForeignKey(User, related_name='gtdb_news_user')
        
    def content_short(self):
        return (self.content[:48] + '..') if len(self.content) > 50 else self.content
    
    def __str__(self):
        return self.headline
    
@python_2_unicode_compatible
class Game(Entity):
    title = models.CharField(max_length=200)
    description = models.TextField()
    reporter = models.CharField(max_length=50)#models.ForeignKey(User, related_name='gtdb_news_user')
        
    def content_short(self):
        return (self.content[:48] + '..') if len(self.content) > 50 else self.content
    
    def __str__(self):
        return self.headline'''
    