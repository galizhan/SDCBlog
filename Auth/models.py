from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    avatar = models.ImageField(upload_to="user_images", null=True)
