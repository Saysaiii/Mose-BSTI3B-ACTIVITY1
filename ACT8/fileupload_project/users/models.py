from django.contrib.auth.models import AbstractUser
from django.db import models

def user_photo_path(instance, filename):
    return f'user_photos/{instance.username}/{filename}'

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to=user_photo_path, null=True, blank=True)
