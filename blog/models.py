# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    """ This is a blog post table database thingy. """

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PanicLevel(models.Model):
    """ This table tracks my panic level as I embark on this journey. """

    level = models.IntegerField()
    description = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=timezone.now)
