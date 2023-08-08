from django import forms
from pokergame.models import GameSession

class GameSessionForm(forms.ModelForm):
    class Meta:
        model = GameSession
        fields = ['game_name']
        labels = {
            'game_name': '게임명(방제)',
        }