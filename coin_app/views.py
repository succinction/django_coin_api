# from django.shortcuts import render
from django.http import JsonResponse
from .models import Game
from django.views.decorators.csrf import csrf_exempt
import datetime
# import json
from django.contrib.auth.models import User
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
            'finalScore': game.finalScore,
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
        'finalScore': game.finalScore,
        'falseCoin': game.falseCoin,
        'measurements': game.measurements,
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def save_game_api(request):
    if request.method == 'POST':

        game = Game()
        user = User.objects.get(username=request.POST.get('userName','guest'))
        game.user = user

        game.gameNumber = int(request.POST.get('gameNumber', None))
        game.date = datetime.datetime.now()
        game.gameType = request.POST.get('gameType', None)
        game.finalScore = request.POST.get('finalScore', None)
        game.falseCoin = request.POST.get('falseCoin', None)
        game.measurements = request.POST.get('measurements', None)
        # game.measurements = urllib.parse.unquote(request.POST.get('measurements', None))

        game.save()
        return JsonResponse({'message': 'success'})

    return JsonResponse({'message': 'fail'})
