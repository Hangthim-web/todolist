from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null = True, blank = True)
    gender = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


