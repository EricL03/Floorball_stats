from django.db import models


class Game(models.Model):
    date = models.DateField()
    opponent = models.CharField(max_length=100)

    our_score = models.PositiveIntegerField(default=0)
    our_score_p1 = models.PositiveIntegerField(default=0)
    our_score_p2 = models.PositiveIntegerField(default=0)
    our_score_p3 = models.PositiveIntegerField(default=0)

    opponent_score = models.PositiveIntegerField(default=0)
    opponent_score_p1 = models.PositiveIntegerField(default=0)
    opponent_score_p2 = models.PositiveIntegerField(default=0)
    opponent_score_p3 = models.PositiveIntegerField(default=0)

    our_shots = models.PositiveIntegerField(default=0)
    our_shots_p1 = models.PositiveIntegerField(default=0)
    our_shots_p2 = models.PositiveIntegerField(default=0)
    our_shots_p3 = models.PositiveIntegerField(default=0)

    opponent_shots = models.PositiveIntegerField(default=0)
    opponent_shots_p1 = models.PositiveIntegerField(default=0)
    opponent_shots_p2 = models.PositiveIntegerField(default=0)
    opponent_shots_p3 = models.PositiveIntegerField(default=0)

    powerplays = models.PositiveIntegerField(default=0)
    powerplay_goals = models.PositiveIntegerField(default=0)
    

    boxplays = models.PositiveIntegerField(default=0)
    boxplay_goals_against = models.PositiveIntegerField(default=0)


    @property
    def shot_percentage(self):
        if self.our_shots == 0: 
            return 0

        return 100 * self.our_score / self.our_shots
    
    @property
    def save_percentage(self):
        if self.opponent_shots == 0: 
            return 0

        return 100 * (1 - self.opponent_score / self.opponent_shots)

    @property
    def shot_save_percentage(self):
        if self.save_percentage == 0: 
            return 0

        return (self.shot_percentage / 100) / (1 - (self.save_percentage / 100))

    @property
    def powerplay_percentage(self):
        if self.powerplays == 0: 
            return 0

        return 100 * self.powerplay_goals / self.powerplays
    
    @property
    def boxplay_percentage(self):
        if self.boxplays == 0: 
            return 0

        return 100 * self.boxplay_goals_against / self.boxplays
    
    def __str__(self):
        return f"{self.date} vs {self.opponent}"
