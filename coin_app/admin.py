from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('finalTime', 'id', 'gameType', 'score', 'numberOfMeasurements', 'gameNumber', 'user', 'date',)


admin.site.register(Game, GameAdmin)
