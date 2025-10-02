from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.games_list, name='list'),
    path('<int:pk>/', views.game_detail, name='detail'),
]
