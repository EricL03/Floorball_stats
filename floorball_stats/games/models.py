from django.db import models


class Game(models.Model):
    date = models.DateField()
    opponent = models.CharField(max_length=100)
    our_score = models.PositiveIntegerField(default=0)
    opponent_score = models.PositiveIntegerField(default=0)
    our_shots = models.PositiveIntegerField(default=0)
    opponent_shots = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.date} vs {self.opponent}"
