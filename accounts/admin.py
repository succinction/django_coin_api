from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class GamesInline(admin.StackedInline):
    model = 'coin_app.Game'
    can_delete = False
    verbose_name_plural = 'Games'


class CustomUserAdmin(BaseUserAdmin):
    inlines = (GamesInline,)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'overall_score', 'score', 'best_score', 'current_streak', 'best_streak', 'wins', 'attempts',)
    # pass

admin.site.register(User, UserAdmin)


