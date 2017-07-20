"""coin_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from coin_app import views as game_views
from accounts.views import register

urlpatterns = [

    # url(r'^$', views.home, name='home')

    url(r'^admin/', admin.site.urls),

    # Accounts
    url(r'^accounts/register/', register, name='register'),

    # API
    url(r'^api/gamelist/', game_views.game_list_api, name='gamelist_api'),

    url(r'^api/leaderboard/', game_views.leaderboard_api, name='leaderboard_api'),

    url(r'^api/game/(?P<id>[-\w]+)/?$', game_views.game_api, name='game_api'),

    url(r'^api/savegame/$', game_views.save_game_api, name='save_game_api'),
]
