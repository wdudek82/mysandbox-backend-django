from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.html import mark_safe
from behaviors.behaviors import Timestamped


class CommonCategory(Timestamped):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class CommonMessage(Timestamped):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

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

# TODO: Add custom manager to filter "published" posts

class Post(CommonMessage):
    image = models.ImageField(upload_to='post/', null=True, blank=True)
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='category')
    tags = models.ManyToManyField('Tag', blank=True)
    publication_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_publication_status(self):
        if self.publication_date and self.publication_date <= timezone.now():
            return mark_safe('<strong style="color: green;">published</strong>')
        else:
            return mark_safe('<strong style="color: orangered;">draft</strong>')
    get_publication_status.short_description = 'publication status'


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