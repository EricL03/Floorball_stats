from django.urls import path
from . import views

app_name = "stats"

urlpatterns = [
    path("", views.stats, name="stats"),
    path("advanced_stats", views.advanced_stats, name="advanced_stats"),
]
