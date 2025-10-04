from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

def player_list(request):
    players = Player.objects.all()
    return render(request, "players/list.html", {"players": players})


def player_add(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("players:list")
    else:
        form = PlayerForm()

    return render(request, "players/form.html", {"form": form})
