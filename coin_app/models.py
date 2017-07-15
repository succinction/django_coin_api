from django.db import models
from accounts.models import User


class Game(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name='games')
    gameNumber = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    gameType = models.PositiveSmallIntegerField()
    numberOfMeasurements = models.PositiveSmallIntegerField()

    # finalTime = models.PositiveSmallIntegerField()
    # finalTime = models.DurationField()
    finalTime = models.CharField(max_length=16)

    duration = models.PositiveSmallIntegerField()
    cheat = models.BooleanField(default=False)

    falseCoin = models.CharField(max_length=4)
    measurements = models.TextField()

    class Meta:
        ordering = ['-date']
    
    def __str__(self, gameNumber=gameNumber, user=user):
        return "Game object {} {}".format(gameNumber, user)


#
# class Example(models.Model):
#     name = models.CharField()
#     mtm = models.ManyToManyField(Game, ThruTable)
#
#
# class ThruTable(models.Model):
#     relate = models.CharField()
#     examlp = models.ForeignKey(Example)
#     gam = models.ForeignKey(Game)

