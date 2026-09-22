from django.shortcuts import render
from django.http import HttpResponse

def song_list(request):
    response_text = '<h1>List of songs</h1>'
    return HttpResponse(response_text)

def song_detail(request, song_id):
    response_text = f"You are calling:{song_id}"
    return HttpResponse(response_text)