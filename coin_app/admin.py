from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('finalScore', 'user', 'gameType', 'date',)


admin.site.register(Game, GameAdmin)
