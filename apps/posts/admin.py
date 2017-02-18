from django.contrib import admin
from django.utils import timezone
from django.utils.html import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Comment, Post, Tag


class MessageMixin:
    def get_image(self, instance):
        image = instance.image
        return mark_safe('<img src="{}" style="max-width: 200px;">'.format(image.url)) if image else None
    get_image.short_description = 'image'

    actions = ['archive_selected']

    def archive_selected(self, request, queryset):
        for instance in queryset:
            instance.archived = True
            instance.archived_at = timezone.now()
            instance.save()
    archive_selected.short_description = 'Archive selected posts'


class AbstractCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created', 'changed', 'modified')
    list_display_links = ('name',)
    list_filter = ('created', 'modified',)
    search_fields = ('name', 'description')
    exclude = ('modified',)


class CommentAdmin(admin.ModelAdmin, MessageMixin):
    list_display = ('id', 'author', 'title', 'content', 'likes', 'dislikes', 'created', 'changed', 'modified',
                    'archived', 'archived_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author__username', 'created', 'modified')
    search_fields = ('title', 'content',)
    exclude = ('modified',)


class PostAdmin(SummernoteModelAdmin, MessageMixin):
    list_display = ('id', 'author', 'title', 'content', 'likes', 'dislikes', 'category', 'get_image',
                    'publication_status', 'published_at', 'created', 'changed', 'modified', 'archived', 'archived_at')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', )
    list_filter = ('author__username', 'category', 'tags', 'likes', 'dislikes', 'publication_status', 'published_at',
                   'created', 'modified', 'archived', 'archived_at')
    search_fields = ('title', 'content')
    exclude = ('modified',)


admin.site.register(Category, AbstractCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, AbstractCategoryAdmin)
