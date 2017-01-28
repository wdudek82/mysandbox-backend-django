from django.contrib import admin
from django.utils.html import mark_safe
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_color', 'image']
    list_display_links = ['user']

    def get_color(self, instance):
        return mark_safe(
            '<div style="margin: auto; background: {}; width: 60px; height: 20px;"></div>'.format(instance.color))
    get_color.short_description = 'color'


admin.site.register(Profile, ProfileAdmin)