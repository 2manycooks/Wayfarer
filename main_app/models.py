from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=’profile_image’, blank=True)
    current_city = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to=’post_image’, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def Meta:
        ordering = ['-created_at']

class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=’city_image’, blank=True)
