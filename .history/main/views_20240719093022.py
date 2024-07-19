from django.shortcuts import render, redirect
from . import models


def blogs(request):
    context = {
        'list':'mashinalar royhati'
    }
    return render(request, 'blog.html', context)


def blog_detail(request, id):
    context = {
        'list2':'Kompaniyalar royxati'
    }
    return render(request, 'blog-detail.html', context)


def comment_create(request):
    context = {

    }
    return render

