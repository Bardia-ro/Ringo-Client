from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#adding comment to check something
class User(AbstractUser):
    bio = models.TextField()