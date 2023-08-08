from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..forms import GameSessionForm
from ..models import GameSession

@login_required(login_url='common:login')
def session_create(request):
    if request.method == 'POST':
        form = GameSessionForm(request.POST)
        if form.is_valid():
            game_session = form.save(commit=False)
            game_session.creator = request.user
            game_session.created_at = timezone.now()
            game_session.save()
            return redirect('pokergame:session_enter', game_session_id=game_session.id)
    else:
        form = GameSessionForm()
    context = {'form': form}
    return render(request, 'pokergame/game_session_form.html', context)

@login_required(login_url='common:login')
def session_enter(request, game_session_id):
    game_session = get_object_or_404(GameSession, pk=game_session_id)
    context = {'game_session' : game_session}
    return render(request, 'pokergame/game_session.html', context)

@login_required(login_url='common:login')
def session_delete(request, game_session_id):
    game_session = get_object_or_404(GameSession, pk=game_session_id)
    if request.user != game_session.creator:
        messages.error(request, '방장만 세션을 종료할 수 있습니다.')
        return redirect('pokergame:session_enter', game_session_id=game_session.id)
    game_session.delete()
    return redirect('pokergame:index')