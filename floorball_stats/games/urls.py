from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.games_list, name='list'),
    path('add/', views.game_add, name='add'),
    path('<int:pk>/', views.game_detail, name='detail'),
    path('<int:pk>/delete/', views.game_delete, name='delete'),
]
