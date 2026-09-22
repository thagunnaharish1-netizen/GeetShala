from django.shortcuts import render

# Create your views here.
def song_list(request):
    # Logic to retrieve and display a list of songs
    return render(request, 'songs/song_list.html')