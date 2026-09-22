# App-level URLconf: routes to specific views within the songs app
from django.urls import path
from . import views
urlpatterns = [
    path('', views.song_list, name='song_list'),  # e.g., /songs/
]