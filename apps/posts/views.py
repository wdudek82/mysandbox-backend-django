import calendar
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db import models
from .models import Category, Comment, Post, Tag


def post_create(request):
    pass


def posts_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


def posts_list(request, category_slug=None):
    categories = Category.objects.all()
    published_posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')

    page = {
        'title': 'All Entries',
        'months_names': (calendar.month_name[num] for num in range(1, 13)),
    }

    if category_slug:
        published_posts = published_posts.filter(category__slug=category_slug)

        try:
            selected_category = Category.objects.get(slug=category_slug)
            page['title'] += f' in category "{selected_category.name}"'
        except models.ObjectDoesNotExist as e:
            page['title'] = 'No such category exists!'

    tags = Tag.objects.all()


    context = {
        'categories': categories,
        'page': page,
        'published_posts': published_posts,
        'tags': tags,
    }
    return render(request, 'posts/post_list.html', context)

def posts_in_category(request, category_id=None):
    posts_in_category = Post.objects.filter(category=category_id)
    page = {
        'title': 'All Entries'
    }

    context = {
        'page': page,
        'posts_in_category': posts_in_category,
    }
    return render(request, 'posts/post_list.html', conte)


def post_update(request, pk=None):
    pass


def post_delete(request, pk=None):
    pass
