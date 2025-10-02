from django.shortcuts import render

def player_list(request):
    return render(request, "players/list.html")
