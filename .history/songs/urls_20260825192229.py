from importlib.resources import path

from . import views
urlpatterns = [
    path('', views.song_list, name='song_list'),    
]