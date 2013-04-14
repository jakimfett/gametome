# Admin for app 'gtdb'
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.db import models as fieldmodels
#from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget
from . import models


# Configure your admin interface here.

class URLInline(admin.StackedInline):
    model = models.URLlink
    extra = 0
    fk_name = 'entity'

class ReviewInline(admin.StackedInline):
    model = models.Review
    extra = 0
    fk_name = 'entity'
    readonly_fields = ['created_date', 'updated_date']
    formfield_overrides = {
        fieldmodels.TextField: {'widget': CKEditorWidget(attrs={'cols': 80, 'rows': 30})},
    }
    
class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 0
    fk_name = 'entity'
    readonly_fields = ['created_date', 'updated_date']
    formfield_overrides = {
        fieldmodels.TextField: {'widget': CKEditorWidget(attrs={'cols': 80, 'rows': 30})},
    }
    
class EntityAdmin(admin.ModelAdmin):
    inlines = [URLInline, CommentInline, ReviewInline]
    list_select_related = True
    list_display = ['title', 'created_date', 'reporter', 'desc_short']
    readonly_fields = ['created_date', 'updated_date']
    list_filter = ['content_type']
    formfield_overrides = {
        fieldmodels.TextField: {'widget': CKEditorWidget(attrs={'cols': 80, 'rows': 30})},
    }

class NewsAdmin(EntityAdmin):
    list_filter = []
    
    def queryset(self, request):
        ct = ContentType.objects.get(model='news')
        qs = super(EntityAdmin, self).queryset(request)
        return qs.filter(content_type=ct)

class CompanyAdmin(EntityAdmin):
    list_filter = []
    
    def queryset(self, request):
        ct = ContentType.objects.get(model='company')
        qs = super(EntityAdmin, self).queryset(request)
        return qs.filter(content_type=ct)
    
class GameAdmin(EntityAdmin):
    list_filter = []

class CommentAdmin(EntityAdmin):
    list_filter = []

class ReviewAdmin(EntityAdmin):
    list_filter = []

admin.site.register(models.Entity, EntityAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Game, GameAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.Company, CompanyAdmin)

