import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Category, Post, Tag
from apps.blog.models import About, Social


def get_sidebar_data():
    """
    General information about page: page title (not jumbotron!),
    and sidebar content: about, archival posts, categories, etc.
    """
    categories = Category.objects.all()
    sidebar = {
        'about': About.objects.get(is_current=True),
        'categories': categories,
        'months_names': (calendar.month_name[num] for num in range(1, 13)),
        'title': 'All Entries',
        'tags': Tag.objects.all(),
        'social': Social.objects.filter(visible=True)
    }
    return sidebar


# TODO: add wysiwyg editor to template
@login_required()
def post_create(request):
    pass


def posts_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    sidebar = get_sidebar_data()
    context = {
        'post': post,
        'sidebar': sidebar,
    }
    return render(request, 'posts/post_detail.html', context)


# TODO: custom manager for Post, that filter all posts from a given month
# TODO: rewrite all views as ClassBased Views
# TODO: Add authentication/OAuth
def posts_list(request, category_slug=None):
    published_posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
    sidebar = get_sidebar_data()
    if category_slug:
        published_posts = published_posts.filter(category__slug=category_slug)
        try:
            selected_category = Category.objects.get(slug=category_slug)
            sidebar['title'] += f' in category "{selected_category.name}"'
        except models.ObjectDoesNotExist:
            sidebar['title'] = 'No such category exists!'
    context = {
        'sidebar': sidebar,
        'published_posts': published_posts,
    }
    return render(request, 'posts/post_list.html', context)


@login_required()
def post_update(request, pk=None):
    pass


@login_required()
def post_delete(request, pk=None):
    pass


class PostDelete(LoginRequiredMixin):
    pass
