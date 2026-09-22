from django.shortcuts import render
from django.http import HttpResponse

def song_list(request):
    # response_text = '<h1>List of songs</h1><h2>Click on Song to View Details.</h2>'
    # return HttpResponse(response_text)
    songs = [
        {'id': 1, 'title': 'Song 1', 'artist': 'Artist 1'},
        {'id': 2, 'title': 'Song 2', 'artist': 'Artist 2'},
        {'id': 3, 'title': 'Song 3', 'artist': 'Artist 3'},
        {'id': 4, 'title': 'Song 4', 'artist': 'Artist 4'},
        {'id': 5, 'title': 'Song 5', 'artist': 'Artist 5'},
    ]
    return render(request, 'song_list.html', {'songs1': songs})

def song_detail(request, song_id):
    response_text = f"You are calling:{song_id}"
    return HttpResponse(response_text)