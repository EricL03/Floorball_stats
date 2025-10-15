from django.db.models import Sum, Avg, Count
from games.models import Game
from stats.models import PlayerGameStats
from django.shortcuts import render

def stats(request):
    games = Game.objects.all()
    total_games = games.count()

    # Team-level stats
    team_stats = games.aggregate(
        total_our_score=Sum("our_score"),
        total_opponent_score=Sum("opponent_score"),
        total_our_shots=Sum("our_shots"),
        avg_our_score=Avg("our_score"),
        avg_opponent_score=Avg("opponent_score"),
        avg_our_shots=Avg("our_shots"),
    )

    # Player-level stats (assuming PlayerGameStats model links player ↔ game)
    player_stats = (
        PlayerGameStats.objects
        .values("player__name")
        .annotate(
            games_played=Count("game", distinct=True),
            total_goals=Sum("goals"),
            total_assists=Sum("assists"),
            #total_points=Sum("points"),
            total_penalties=Sum("penalties"),
            total_plus_minus=Sum("plus_minus"),
        )
        .order_by("-games_played")
    )

    context = {
        "total_games": total_games,
        **team_stats,
        "player_stats": player_stats,
    }
    return render(request, "stats/stats.html", context)
