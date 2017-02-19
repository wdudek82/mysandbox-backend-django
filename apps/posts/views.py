import calendar
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.db import models
from .models import Category, Post, Tag
from apps.blog.models import About, Social


def get_page_info():
    """
    General information about page: page title (not jumbotron!), 'about' contentm
    archival posts, etc.
    """
    page = {
        'about': About.objects.get(is_current=True),
        'title': 'All Entries',
        'months_names': (calendar.month_name[num] for num in range(1, 13)),
        'social': Social.objects.filter(visible=True)
    }
    return page


# TODO: add wysiwyg editor to template
def post_create(request):
    pass


def posts_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
        'page': get_page_info(),
    }
    return render(request, 'posts/post_detail.html', context)


# TODO: custom manager for Post, that filter all posts from a given month
# TODO: reqrite all views as ClassBased Views
# TODO: Add authentication/OAuth
def posts_list(request, category_slug=None):
    categories = Category.objects.all()
    published_posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
    page = get_page_info()


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


def post_update(request, pk=None):
    pass


def post_delete(request, pk=None):
    pass
