from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.OneToOneField(User)
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    image = models.ImageField(upload_to='post/', null=True, blank=True)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    draft = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    main_category = models.ForeignKey('Category', null=True, blank=True, related_name='main_category')
    secondary_categories = models.ManyToManyField('Category',
                                                  blank=True,
                                                  related_name='secondary_categories')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# TODO: Create ABC to represent fields common for Post and Comment
class Comment(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    content = models.TextField()
    # likes = models.IntegerField(default=0)
    # dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title