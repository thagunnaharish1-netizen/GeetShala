from django.shortcuts import render
from django.http import HttpResponse

def song_list(request):
    # response_text = '<h1>List of songs</h1><h2>Click on Song to View Details.</h2>'
    # return HttpResponse(response_text)
    songs = []
    return render(request, 'song_list22.html', {'songs': songs})

def song_detail(request, song_id):
    response_text = f"You are calling:{song_id}"
    return HttpResponse(response_text)