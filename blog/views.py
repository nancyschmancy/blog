# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post


def post_list(request):
    """ Displays posts. """

    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/post_list.html', context)