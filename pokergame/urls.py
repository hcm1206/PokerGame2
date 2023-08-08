from django.urls import path

from .views import pokergame_base_views, game_session_views

app_name = 'pokergame'

urlpatterns = [
    # base_views.py
    path('',
         pokergame_base_views.index, name='index'),

    # game_session_views.py
    path('game/create/',
         game_session_views.session_create, name='session_create'),
     path('game/session/<int:game_session_id>/',
         game_session_views.session_enter, name='session_enter'),
    path('game/delete/<int:game_session_id>/',
         game_session_views.session_delete, name='session_delete'),

]