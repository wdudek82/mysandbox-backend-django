from calendar import month_name
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from colorfield.fields import ColorField


class Profile(models.Model):
    DAY_CHOICES = ((day, day) for day in range(1, 32))
    MONTH_CHOICES = ((month, month_name[month]) for month in range(1, 13))
    YEAR_CHOICES = ((year, year) for year in reversed(range(1900, timezone.now().year)))

    user = models.OneToOneField(User)
    color = ColorField()
    image = models.ImageField(upload_to='profile', null=True, blank=True)
    about = models.TextField()
    day_of_birth = models.IntegerField(choices=DAY_CHOICES, default=1)
    month_of_birth = models.IntegerField(choices=MONTH_CHOICES, default=1)
    year_of_birth = models.IntegerField(choices=YEAR_CHOICES, default=timezone.now().year)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    Profile.objects.get_or_create(user=instance)

# post_save.connect(post_save_user_model_receiver, sender=User)