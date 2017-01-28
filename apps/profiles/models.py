from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from colorfield.fields import ColorField


class Profile(models.Model):
    user = models.OneToOneField(User)
    color = ColorField()
    image = models.ImageField(upload_to='profile', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    Profile.objects.get_or_create(user=instance)
# post_save.connect(post_save_user_model_receiver, sender=User)