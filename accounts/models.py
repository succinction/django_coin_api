from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    """
    My custom model

    first_name, last_name, password, username,
    """
    email = models.EmailField(null=True, blank=True)
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    attempts = models.IntegerField(null=True, blank=True)
    wins = models.IntegerField(null=True, blank=True)
    current_streak = models.IntegerField(null=True, blank=True)
    best_streak = models.IntegerField(null=True, blank=True)
    rank = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username