from django.contrib import admin
from django.utils.html import mark_safe
from .models import About, Social


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_content', 'get_image', 'is_current', 'created', 'changed', 'modified')
    exclude = ('modified',)

    def get_content(self, instance):
        return mark_safe(instance.content)
    get_content.short_description = 'content'
    get_content.admin_order_field = 'content'

    def get_image(self, instance):
        html_template = '<img src={} style="max-width: 100px; max-height: 100px; border-radius: 50%">'
        return mark_safe(html_template.format(instance.image.url) if instance.image else '-')
    get_image.short_description = 'image'


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ordering', 'get_font_awesome_icon_tag', 'url', 'visible',
                    'created', 'changed', 'modified')
    list_display_links = ('name',)
    exclude = ('modified',)

    def get_font_awesome_icon_tag(self, instance):
        return mark_safe(instance.font_awesome_icon_tag)
