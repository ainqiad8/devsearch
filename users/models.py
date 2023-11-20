from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=222, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=300, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,upload_to='profiles/', default='profiles/user-default.png' )
    social_twitter = models.CharField(max_length=222, null=True, blank=True)
    social_Linkedin = models.CharField(max_length=222, null=True, blank=True)
    social_github = models.CharField(max_length=222, null=True, blank=True)
    social_Youtube = models.CharField(max_length=222, null=True, blank=True)
    social_Facebook = models.CharField(max_length=222, null=True, blank=True)
    social_website = models.CharField(max_length=222, null=True, blank=True)
    social_Instagram = models.CharField(max_length=222, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)


    def __str__(self):
        return str(self.username)
    
                         


class Skill(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)


    def __str__(self):
        return str(self.name)



