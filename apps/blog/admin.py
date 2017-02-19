from django.contrib import admin
from django.utils.html import mark_safe
from .models import About, Social


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_content', 'is_current', 'created', 'changed', 'modified')
    exclude = ('modified',)

    def get_content(self, instance):
        return mark_safe(instance.content)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ordering', 'get_font_awesome_icon_tag', 'url', 'visible',
                    'created', 'changed', 'modified')
    list_display_links = ('name',)
    exclude = ('modified',)

    def get_font_awesome_icon_tag(self, instance):
        return mark_safe(instance.font_awesome_icon_tag)
