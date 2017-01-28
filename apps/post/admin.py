from django.contrib import admin
from django.utils.html import format_html, format_html_join, mark_safe
from .models import Category, Comment, Post, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content', 'likes', 'dislikes', 'created_at', 'updated_at',
                    'archived', 'archived_at')
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content', 'likes', 'dislikes', 'main_category', 'get_image', 'draft',
                    'published_at', 'created_at', 'updated_at', 'archived', 'archived_at')
    list_display_links = ('title',)
    # list_editable = ('content',)
    filter_horizontal = ('secondary_categories', 'tags', )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author__username', 'main_category', 'draft', 'published_at')
    search_fields = ('title', 'content')

    def get_image(self, instance):
        try:
            # return format_html('<img src="{}">', instance.image.url)
            return mark_safe('<img src="{}" style="max-width: 200px;">'.format(instance.image.url))
        except:
            return None
    get_image.short_description = 'image'


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
