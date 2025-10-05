from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm, PlayerGameStatsFormSet


def games_list(request):
    games = Game.objects.all().order_by('-date')
    return render(request, "games/list.html", {"games": games})


def game_add(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()  # creates the Game
            return redirect('games:detail', pk=game.pk)
    else:
        form = GameForm()

    return render(request, 'games/detail.html', {'form': form, 'formset': None, 'game': None})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        formset = PlayerGameStatsFormSet(request.POST, instance=game)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('games:list')
        else: 
            print("Form errors:", form.errors)
            print("Formset errors:", formset.errors)
    else:
        form = GameForm(instance=game)
        formset = PlayerGameStatsFormSet(instance=game)

    return render(request, 'games/detail.html', {'form': form, 'formset': formset, 'game': game})


def game_delete(request, pk): 
    game = get_object_or_404(Game, pk=pk)
    if game:
        game.delete()
    
    return redirect('games:list')
