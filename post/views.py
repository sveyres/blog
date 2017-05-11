# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from post.models import Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_details(request, p_id):
    post = Post.objects.get(id=p_id)
    return render(request, 'post_details.html', {'post': post})

def post_details_slug(request, p_slug):
    post = Post.objects.get(slug=p_slug)
    return render(request, 'post_details.html', {'post': post})
