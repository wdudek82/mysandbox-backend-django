import datetime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from .models import Badge, Profile, Reputation


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


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


admin.site.register(Badge)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Reputation)