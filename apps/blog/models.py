from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from behaviors.behaviors import Timestamped


# TODO: Add SummernoteModelAdmin (wysywig) to About model
class About(Timestamped):
    content = models.TextField()
    image = models.ImageField(upload_to='about', null=True, blank=True)
    is_current = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'About'
        ordering = ('-is_current',)

    def __str__(self):
        return str(self.id)


class Social(Timestamped):
    name = models.CharField(max_length=255, unique=True)
    ordering = models.IntegerField(unique=True)
    font_awesome_icon_tag = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=1000, unique=True, null=True, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Social'
        ordering = ('ordering',)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=About)
def set_is_current(sender, instance, *args, **kwargs):
    """
    Only one current 'about' item is allowed, so if any is selected as is_current=True
    automatically all other will be set as is_current=False 
    """
    if instance.is_current:
        About.objects.exclude(id=instance.id).update(is_current=False)