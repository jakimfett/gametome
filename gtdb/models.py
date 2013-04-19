from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation

# Monkey-patching the User object
@property
def prettyname(self):
    if self.get_full_name():
        return self.get_full_name()
    return self.username 
User.name = prettyname

# Create your models here.
@python_2_unicode_compatible
class Entity(models.Model):
    title = models.CharField(max_length=255)
    short = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)
    reporter = models.ForeignKey(User)
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

class Game(Entity):
    cost = models.CharField(max_length=255)
    version = models.CharField(max_length=255)

    def get_absolute_url(self):
        return "/games/%d/" % (self.pk)

class Review(Entity):
    entity = models.ForeignKey(Entity, related_name='reviews')
    score = models.IntegerField()

class Company(Entity):
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return "/company/%d/" % (self.pk)


    