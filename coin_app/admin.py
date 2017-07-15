from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('finalTime', 'numberOfMeasurements', 'gameNumber', 'user', 'gameType', 'date',)


admin.site.register(Game, GameAdmin)
