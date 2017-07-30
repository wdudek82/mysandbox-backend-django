from django.contrib import admin
from .models import Smog, Weather


class SmogAdmin(admin.ModelAdmin):
    pass


class WetherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Smog)
admin.site.register(Weather)