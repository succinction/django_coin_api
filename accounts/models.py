from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """
    My custom model

    first_name, last_name, password, username,
    """
    email = models.EmailField(null=True, blank=True)
    score = models.FloatField(default=0)
    best_score = models.FloatField(default=0)
    attempts = models.PositiveSmallIntegerField(default=0)
    wins = models.PositiveSmallIntegerField(default=0)
    current_streak = models.PositiveSmallIntegerField(default=0)
    best_streak = models.PositiveSmallIntegerField(default=0)
    rank = models.PositiveSmallIntegerField(null=True, blank=True)

    is_guest = models.BooleanField(default=True)
    guest_number = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.username
