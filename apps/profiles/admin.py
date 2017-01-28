import datetime
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_color', 'get_image', 'about', 'get_birth_date']
    list_display_links = ['user']

    def get_color(self, instance):
        return mark_safe(f'<div style="margin: auto; background: {instance.color}; width: 60px; height: 20px;"></div>')
    get_color.short_description = 'color'

    def get_image(self, instance):
        return mark_safe(f'<img src="{instance.image.url}">') if instance.image else '-'
    get_image.short_description = 'image'

    def get_birth_date(self, instance):
        return datetime.date(
            instance.year_of_birth,
            instance.month_of_birth,
            instance.day_of_birth).strftime('%d %B %Y (%A)')
    get_birth_date.short_description = 'date of birth'


admin.site.register(Profile, ProfileAdmin)