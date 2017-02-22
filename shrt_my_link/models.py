from __future__ import unicode_literals

from django.db import models

class Link(models.Model):
    url = models.URLField(max_length=200)
    token = models.CharField(max_length=200)
    clickCount = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %d' % (self.url, self.token, self.clickCount)
