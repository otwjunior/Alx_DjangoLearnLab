from django.db.models.signals import post_save
from django.dispatch import  receiver
from django.contrib.auth.models import User
from .models import  Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    #ensure user has profile before trying to save it
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        #if profile does not exist  create one
        Profile.objects.create(user=instance)