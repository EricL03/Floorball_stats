from django import forms
from .models import Game
from stats.models import PlayerGameStats
from players.models import Player


class PlayerGameStatsForm(forms.ModelForm):
    points = forms.IntegerField(required=False, disabled=True, label="Poäng")

    class Meta:
        model = PlayerGameStats
        fields = ["player", "goals", "assists", "points", "penalties", "plus_minus"]

    def __init__(self, *args, **kwargs):
        game = kwargs.pop("game", None)
        super().__init__(*args, **kwargs)

        # populate points field from instance
        if self.instance and self.instance.pk:
            self.fields["points"].initial = self.instance.points

        if game:
            # Get IDs of all other players in this game
            existing_players = PlayerGameStats.objects.filter(game=game)
            if self.instance and self.instance.pk:
                # Exclude current instance's player from the filter
                existing_players = existing_players.exclude(pk=self.instance.pk)
            existing_ids = existing_players.values_list("player_id", flat=True)

            # Filter queryset to exclude only the other players
            self.fields["player"].queryset = Player.objects.exclude(id__in=existing_ids)


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'opponent', 'our_score', 'our_score_p1', 'our_score_p2', 'our_score_p3',
                  'opponent_score', 'opponent_score_p1', 'opponent_score_p2', 'opponent_score_p3', 
                  'our_shots', 'our_shots_p1', 'our_shots_p2', 'our_shots_p3', 'opponent_shots', 
                  'opponent_shots_p1', 'opponent_shots_p2', 'opponent_shots_p3', 'powerplays', 
                  'powerplay_goals', 'boxplays', 'boxplay_goals_against']


PlayerGameStatsFormSet = forms.inlineformset_factory(
    Game,
    PlayerGameStats,
    form=PlayerGameStatsForm,
    fields=['player', 'goals', 'assists', 'points', 'penalties', 'plus_minus'],
    extra=0,
    can_delete=True
)
