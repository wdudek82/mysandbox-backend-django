from django.contrib import admin
from django.utils import timezone
from django.utils.html import mark_safe
from .models import Category, Comment, Post, Tag


class Mixins:
    def get_image(self, instance):
        try:
            return mark_safe('<img src="{}" style="max-width: 200px;">'.format(instance.image.url))
        except:
            return None
    get_image.short_description = 'image'

    actions = ['archive_selected']

    def archive_selected(self, request, queryset):
        for instance in queryset:
            instance.archived = True
            instance.archived_at = timezone.now()
            instance.save()
    archive_selected.short_description = 'Archive selected posts'


class CommonCategoryAdmin(admin.ModelAdmin, Mixins):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('name', 'description')


class CommonMessageAdmin(Mixins):
    list_display = ['id', 'author', 'title', 'content', 'likes', 'dislikes', 'created_at', 'updated_at',
                    'archived', 'archived_at']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author__username', 'created_at', 'updated_at')
    search_fields = ('title', 'content',)


class CommentAdmin(admin.ModelAdmin, CommonMessageAdmin):
    list_display = ('id', 'author', 'title', 'content', 'likes', 'dislikes', 'created_at', 'updated_at',
                    'archived', 'archived_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author__username', 'created_at', 'updated_at')
    search_fields = ('title', 'content',)


class PostAdmin(admin.ModelAdmin, CommonMessageAdmin):
    list_display = ['id', 'author', 'title', 'content', 'likes', 'dislikes', 'category', 'get_image', 'draft',
                    'published_at', 'created_at', 'updated_at', 'archived', 'archived_at']
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', )
    list_filter = ('author__username', 'category', 'draft', 'likes', 'dislikes', 'published_at',
                   'created_at', 'updated_at', 'archived', 'archived_at')
    search_fields = ('title', 'content')


admin.site.register(Category, CommonCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, CommonCategoryAdmin)
