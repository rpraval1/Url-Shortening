from django.contrib import admin

from .models import Link

class LinksAdmin(admin.ModelAdmin):
    list_display = ['url', 'token', 'clickCount']

admin.site.register(Link, LinksAdmin)
