# import uuid
from django.db import models

from django.contrib.auth.models import User


class Game(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, blank=True, null=True)
    gameNumber = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    gameType = models.PositiveSmallIntegerField()
    finalScore = models.CharField(max_length=24)
    falseCoin = models.CharField(max_length=4)
    measurements = models.TextField()
    
    def __str__(self, gameNumber=gameNumber, user=user):
        return "Game object {} {}".format(gameNumber, user)

