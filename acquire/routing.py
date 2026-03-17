from django.urls import re_path

from game.consumers import GameConsumer
from matcha.consumers import MatchaConsumer


websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<game_pk>[^/]+)/$', GameConsumer.as_asgi()),
    re_path(r'^ws/matcha/(?P<game_name>[^/]+)/$', MatchaConsumer.as_asgi()),
]
