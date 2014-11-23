from django.contrib import admin
from .models import TimeLineEvent, Url


class UrlInline(admin.TabularInline):
    model = Url


admin.site.register(TimeLineEvent, inlines=[UrlInline])
admin.site.register(Url)
