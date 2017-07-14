from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class GamesInline(admin.StackedInline):
    model = 'coin_app.Game'
    can_delete = False
    verbose_name_plural = 'Games'


class CustomUserAdmin(BaseUserAdmin):
    inlines = (GamesInline,)


admin.site.register(User)


