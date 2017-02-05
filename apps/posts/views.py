from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post


def posts_home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'base.html', context)

def posts_detail(request, pk=None):
    print(pk)
    return render(request, 'base.html', {})