from django.contrib import admin
from .models import GameSession

class GameSessionAdmin(admin.ModelAdmin):
    search_fields = ['game_name']

admin.site.register(GameSession, GameSessionAdmin)

# Register your models here.
