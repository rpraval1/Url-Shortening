from django.contrib import admin

from .models import Link

class LinksAdmin(admin.ModelAdmin):
    list_display = ['url', 'token', 'count']

admin.site.register(Link, LinksAdmin)
