from __future__ import unicode_literals

from django.db import models

class Link(models.Model):
    url = models.URLField(max_length=200)
    token = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.url, self.token)
