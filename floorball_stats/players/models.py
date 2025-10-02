from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    jersey_number = models.PositiveIntegerField()
    position = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} #{self.jersey_number}"
