from games.models import Game
from stats.models import PlayerGameStats
from django.shortcuts import render


def stats(request):
    games = Game.objects.all()
    total_games = games.count()

    if total_games == 0:
        context = {"total_games": 0}
        return render(request, "stats/stats.html", context)

    # ---------- TEAM AVERAGES ----------
    avg_our_score = sum(g.our_score for g in games) / total_games
    avg_opponent_score = sum(g.opponent_score for g in games) / total_games

    avg_our_score_p1 = sum(g.our_score_p1 for g in games) / total_games
    avg_our_score_p2 = sum(g.our_score_p2 for g in games) / total_games
    avg_our_score_p3 = sum(g.our_score_p3 for g in games) / total_games

    avg_opponent_score_p1 = sum(g.opponent_score_p1 for g in games) / total_games
    avg_opponent_score_p2 = sum(g.opponent_score_p2 for g in games) / total_games
    avg_opponent_score_p3 = sum(g.opponent_score_p3 for g in games) / total_games

    avg_our_shots = sum(g.our_shots for g in games) / total_games
    avg_opponent_shots = sum(g.opponent_shots for g in games) / total_games

    avg_our_shots_p1 = sum(g.our_shots_p1 for g in games) / total_games
    avg_our_shots_p2 = sum(g.our_shots_p2 for g in games) / total_games
    avg_our_shots_p3 = sum(g.our_shots_p3 for g in games) / total_games

    avg_opponent_shots_p1 = sum(g.opponent_shots_p1 for g in games) / total_games
    avg_opponent_shots_p2 = sum(g.opponent_shots_p2 for g in games) / total_games
    avg_opponent_shots_p3 = sum(g.opponent_shots_p3 for g in games) / total_games

    # ---------- DETAIL BOXES ----------
    total_powerplays = sum(g.powerplays for g in games)
    total_powerplay_goals = sum(g.powerplay_goals for g in games)
    total_boxplays = sum(g.boxplays for g in games)
    total_boxplay_goals_against = sum(g.boxplay_goals_against for g in games)

    # ---------- PROPERTY-BASED AVERAGES ----------
    avg_shot_percentage = sum(g.shot_percentage for g in games) / total_games
    avg_save_percentage = sum(g.save_percentage for g in games) / total_games
    avg_shot_save_percentage = sum(g.shot_save_percentage for g in games) / total_games
    avg_powerplay_percentage = 100 * total_powerplay_goals / total_powerplays 
    avg_boxplay_percentage = 100 * (1 - total_boxplay_goals_against / total_boxplays)

    # ---------- PLAYER STATS ----------
    player_stats_raw = PlayerGameStats.objects.select_related("player", "game")
    player_map = {}

    for stat in player_stats_raw:
        name = stat.player.name
        if name not in player_map:
            player_map[name] = {
                "games_played": set(),
                "goals": 0,
                "assists": 0,
                "points": 0,
                "penalties": 0,
                "plus_minus": 0,
            }

        entry = player_map[name]
        entry["games_played"].add(stat.game_id)
        entry["goals"] += stat.goals
        entry["assists"] += stat.assists
        # Handle property "points"
        entry["points"] += stat.points if hasattr(stat, "points") else (stat.goals + stat.assists)
        entry["penalties"] += stat.penalties
        entry["plus_minus"] += stat.plus_minus

    # Convert sets to counts
    player_stats = []
    for name, stats in player_map.items():
        player_stats.append({
            "player_name": name,
            "games_played": len(stats["games_played"]),
            "goals": stats["goals"],
            "assists": stats["assists"],
            "points": stats["points"],
            "penalties": stats["penalties"],
            "plus_minus": stats["plus_minus"],
        })

    player_stats.sort(key=lambda p: p["points"], reverse=True)

    # ---------- CONTEXT ----------
    context = {
        "total_games": total_games,
        "avg_our_score": avg_our_score,
        "avg_opponent_score": avg_opponent_score,
        "avg_our_score_p1": avg_our_score_p1,
        "avg_our_score_p2": avg_our_score_p2,
        "avg_our_score_p3": avg_our_score_p3,
        "avg_opponent_score_p1": avg_opponent_score_p1,
        "avg_opponent_score_p2": avg_opponent_score_p2,
        "avg_opponent_score_p3": avg_opponent_score_p3,
        "avg_our_shots": avg_our_shots,
        "avg_opponent_shots": avg_opponent_shots,
        "avg_our_shots_p1": avg_our_shots_p1,
        "avg_our_shots_p2": avg_our_shots_p2,
        "avg_our_shots_p3": avg_our_shots_p3,
        "avg_opponent_shots_p1": avg_opponent_shots_p1,
        "avg_opponent_shots_p2": avg_opponent_shots_p2,
        "avg_opponent_shots_p3": avg_opponent_shots_p3,
        "avg_shot_percentage": avg_shot_percentage,
        "avg_save_percentage": avg_save_percentage,
        "avg_shot_save_percentage": avg_shot_save_percentage,
        "avg_powerplay_percentage": avg_powerplay_percentage,
        "avg_boxplay_percentage": avg_boxplay_percentage,
        "total_powerplays": total_powerplays,
        "total_powerplay_goals": total_powerplay_goals,
        "total_boxplays": total_boxplays,
        "total_boxplay_goals_against": total_boxplay_goals_against,
        "player_stats": player_stats,
    }

    return render(request, "stats/stats.html", context)
