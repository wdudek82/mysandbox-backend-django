from django.shortcuts import render
from .models import Post


def post_create(request):
    pass


def posts_detail(request, pk=None):
    print(pk)
    return render(request, 'base.html', {})


def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'base.html', context)


def post_update(request, pk=None):
    pass


def post_delete(request, pk=None):
    pass




