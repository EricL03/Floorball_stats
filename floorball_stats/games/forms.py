from django import forms
from .models import Game
from stats.models import PlayerGameStats


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'opponent', 'our_score', 'opponent_score', 'our_shots', 'opponent_shots']


PlayerGameStatsFormSet = forms.inlineformset_factory(
    Game,
    PlayerGameStats,
    fields=['player', 'goals', 'assists', 'penalties'],
    extra=1,
    can_delete=True
)
