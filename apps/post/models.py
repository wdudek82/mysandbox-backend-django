from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class CommonCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CommonMessage(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    archived_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Category(CommonCategory):

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Comment(CommonMessage):
    post = models.ForeignKey('Post')

    def __str__(self):
        return self.title


class Post(CommonMessage):
    image = models.ImageField(upload_to='post/', null=True, blank=True)
    main_category = models.ForeignKey('Category', null=True, blank=True, related_name='main_category')
    secondary_categories = models.ManyToManyField('Category',
                                                  blank=True,
                                                  related_name='secondary_categories')
    tags = models.ManyToManyField('Tag', blank=True)
    draft = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(CommonCategory):

    def __str__(self):
        return self.name


