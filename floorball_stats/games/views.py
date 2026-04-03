from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm, PlayerGameStatsFormSet
from stats.models import PlayerGameStats
from datetime import date


def games_list(request):
    games = Game.objects.all().order_by("-date")
    return render(request, "games/list.html", {"games": games})


def game_add(request):
    today = date.today()
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()  # creates the Game
            return redirect("games:detail", pk=game.pk)
    else:
        form = GameForm()

    return render(
        request,
        "games/detail.html",
        {"form": form, "formset": None, "game": None, "today": today},
    )


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    today = date.today()
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        formset = PlayerGameStatsFormSet(
            request.POST, instance=game, form_kwargs={"game": game}
        )

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("games:list")
        else:
            print("Form errors:", form.errors)
            print("Formset errors:", formset.errors)
    else:
        form = GameForm(instance=game)
        formset = PlayerGameStatsFormSet(instance=game, form_kwargs={"game": game})

    return render(
        request,
        "games/detail.html",
        {"form": form, "formset": formset, "game": game, "today": today},
    )


def game_view(request, pk):
    game = get_object_or_404(Game, pk=pk)
    player_stats = PlayerGameStats.objects.filter(game=game).select_related("player")

    return render(
        request,
        "games/game_view.html",
        {
            "game": game,
            "player_stats": player_stats,
        },
    )


def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if game:
        game.delete()

    return redirect("games:list")
