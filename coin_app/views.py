# from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .models import Game
from django.views.decorators.csrf import csrf_exempt
import datetime
# import json
from accounts.models import User

# from lazysignup.decorators import allow_lazy_user


# import urllib

# {"userName":"guest","gameNumber":1,"gameType":9,"falseCoin":"1+","finalScore":"0/3=0:04","measurements":[{"time":"0:04","ankh":[30,0],"feather":[593,0],"coin8":[588,-309],"coin7":[528,-211],"coin6":[214,-233],"coin5":[65,-298],"coin4":[316,0],"coin3":[263,0],"coin2":[210,0],"coin1":[156,0],"coin0":[103,0]}]}


@csrf_exempt
def game_list_api(request):
    games = Game.objects.all()
    data = []
    for game in games:
        data.append({
            'userName': game.user.username,
            'gameNumber': game.gameNumber,
            'date': game.date,
            'gameType': game.gameType,
            'numberOfMeasurements': game.numberOfMeasurements,
            'finalTime': game.finalTime,

        })
    return JsonResponse(data, safe=False)


@csrf_exempt
def game_api(request, gameNumber):
    game = Game.objects.get(gameNumber=gameNumber)
    data = {
        'user': game.user.username,
        'gameNumber': game.gameNumber,
        'date': game.date,
        'gameType': game.gameType,
        'numberOfMeasurements': game.numberOfMeasurements,
        'finalTime': game.finalTime,
        'falseCoin': game.falseCoin,
        'measurements': game.measurements,
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
# @allow_lazy_user
def save_game_api(request):

    if request.method == 'POST':
        game = Game()

        user = User.objects.get(username=request.POST.get('userName', 'default'))

        if user.username == 'guest' or user.username == 'default':
        # if request.user.is_anonymous():
            anaons = User.objects.filter(is_guest=True).latest('guest_number')
            next_guest = anaons.guest_number + 1
            user = User()
            user.username = f'Guest_{next_guest}'
            user.set_password('guest123')
            user.is_guest = True
            user.guest_number = next_guest
            user.save()
            login(request, user)
        # else:
        #     user = User.objects.get(username=request.POST.get('userName', 'default'))

        game.user = user
        game.score = request.POST.get('score', 0)

        game.gameNumber = int(request.POST.get('gameNumber', None))
        game.date = datetime.datetime.now()
        game.gameType = request.POST.get('gameType', None)
        game.numberOfMeasurements = request.POST.get('numberOfMeasurements', None)
        game.finalTime = request.POST.get('finalTime', None)

        game.falseCoin = request.POST.get('falseCoin', None)
        game.measurements = request.POST.get('measurements', None)
        # game.measurements = urllib.parse.unquote(request.POST.get('measurements', None))

        game.save()

        # SCORE LOGIC
        user.attempts += 1
        won = 1 if int(game.score) == 1 else 0
        user.wins += won
        user.current_streak = user.current_streak + won if won == 1 else 0
        user.best_streak = user.current_streak if user.current_streak > user.best_streak else user.best_streak
        user.save()



        return JsonResponse({'message': 'success', 'newGuest': user.username})

    return JsonResponse({'message': 'fail'})
