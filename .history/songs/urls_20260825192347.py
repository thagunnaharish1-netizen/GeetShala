from importlib.resources import path

from songs import views
urlpatterns = [
    path('', views.song_list, name='song_list'),    
]