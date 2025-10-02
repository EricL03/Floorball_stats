from django.shortcuts import render

def games_list(request):
    return render(request, "games/list.html")

def game_detail(request, pk):
    return render(request, "games/detail.html", {"pk": pk})
