from django.shortcuts import render

from ..models import GameSession


def index(request):
    session_list = GameSession.objects.order_by('created_at')
    context = {'game_session_list': session_list}
    return render(request, 'pokergame/game_list.html', context)