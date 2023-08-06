from django.shortcuts import render


def index(request):
    return render(request, 'pokergame/game_list.html')