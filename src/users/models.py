from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)


from .signals import *
