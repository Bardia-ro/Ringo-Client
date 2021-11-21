from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#adding comment to check something
#new commit
class User(AbstractUser):
    bio = models.TextField()