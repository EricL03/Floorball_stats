from django.db import models
from players.models import Player
from games.models import Game


class PlayerGameStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="stats")
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    penalties = models.PositiveIntegerField(default=0)
    plus_minus = models.IntegerField(default=0)

    class Meta:
        unique_together = ('player', 'game')  # Prevent duplicate entries

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.player} in {self.game}"
