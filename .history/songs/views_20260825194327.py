from django.shortcuts import render
from django.http import HttpResponse

def song_list(request):
    response_text = 'List of songs'
    return HttpResponse(response_text)

def song_detail(request, id):
    format_id = id