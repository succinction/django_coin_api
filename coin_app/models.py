# import uuid
from django.db import models
from accounts.models import User


class Game(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, blank=True, null=True, related_name='games')
    gameNumber = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    gameType = models.PositiveSmallIntegerField()
    # finalScore = models.CharField(max_length=24)

    # totalCoins = models.PositiveSmallIntegerField()
    numberOfMeasurements = models.PositiveSmallIntegerField()
    finalTime = models.CharField(max_length=16)

    falseCoin = models.CharField(max_length=4)
    measurements = models.TextField()

    class Meta:
        ordering = ['-date']
    
    def __str__(self, gameNumber=gameNumber, user=user):
        return "Game object {} {}".format(gameNumber, user)

