from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('gameNumber', 'user', 'gameType', 'finalScore')


admin.site.register(Game, GameAdmin)
