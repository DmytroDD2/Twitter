from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cover_image = models.ImageField(upload_to="user_auth/covers", null=True, blank=True)
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    date_joined = models.DateField(auto_now_add=True)

    crea_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')

    def __str__(self):
        return f'{self.username}'
