from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from .models import Profiles



def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profiles.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


#@receiver(post_save, sender=Profiles)
def deleteuser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    



post_save.connect(createProfile, sender=User)
post_delete.connect(deleteuser, sender= Profiles)