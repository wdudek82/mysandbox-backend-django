from calendar import month_name
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from colorfield.fields import ColorField


def get_sentinel_reputation():
    sentinel_reputation = Reputation.objects.get_or_create(name='Unknown Wanderer')[0]
    sentinel_reputation.description = 'Replace this with actual description!'
    sentinel_reputation.save()
    return sentinel_reputation


class Badge(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.id)


class Profile(models.Model):
    DAY_CHOICES = ((day, day) for day in range(1, 32))
    MONTH_CHOICES = ((month, month_name[month]) for month in range(1, 13))
    YEAR_CHOICES = ((year, year) for year in reversed(range(1900, timezone.now().year+1)))

    user = models.OneToOneField(User)
    color = ColorField()
    image = models.ImageField(upload_to='profile', null=True, blank=True)
    about = models.TextField()
    level = models.IntegerField(default=1)
    reputation = models.ForeignKey('Reputation', null=True, blank=True, on_delete=models.SET_NULL)
    badges = models.ManyToManyField(Badge)
    day_of_birth = models.IntegerField(choices=DAY_CHOICES, default=1)
    month_of_birth = models.IntegerField(choices=MONTH_CHOICES, default=1)
    year_of_birth = models.IntegerField(choices=YEAR_CHOICES, default=timezone.now().year)

    def __str__(self):
        return self.user.username


class Reputation(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Reputation'

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    Profile.objects.get_or_create(user=instance)

# post_save.connect(post_save_user_model_receiver, sender=User)