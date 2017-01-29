from __future__ import unicode_literals
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User


class CommonCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
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
    archived_at = models.DateTimeField(null=True, blank=True, editable=False)

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
    category = models.ForeignKey('Category', null=True, blank=True, related_name='category')
    tags = models.ManyToManyField('Tag', blank=True)
    draft = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.title


class Tag(CommonCategory):

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Post)
@receiver(pre_save, sender=Comment)
def set_archived(sender, instance, *args, **kwargs):
    if not instance.archived:
        instance.archived_at = None
    elif instance.archived and not instance.archived_at:
        instance.archived_at = timezone.now()

# pre_save.connect(set_archived, sender=Post)
# pre_save.connect(set_archived, sender=Comment)