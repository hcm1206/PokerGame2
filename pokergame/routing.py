from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/pokergame/game/session/(?P<game_session_id>\d+)/$', consumers.SessionConsumer.as_asgi()),
]