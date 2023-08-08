from django.db import models
from django.contrib.auth.models import User

class GameSession(models.Model):
    game_name = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_game')
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='game_participants', blank=True)

    
    def __str__(self):
        return self.game_name

# Create your models here.
