import requests
from django.http import HttpResponse
from django.shortcuts import redirect, render

POCKEMON_URL = 'https://pokeapi.co/api/v2/'


def index(request):
    context = {"title": "Home", "link_text": "Show me all pokemons"}
    return HttpResponse(render(request, 'pockemon/index.html', context))


def take_all_names(request):
    response = requests.get(f'{POCKEMON_URL}/type/3').json()
    pokemons_names = [p['pokemon']['name'] for p in response['pokemon']]
    return HttpResponse(render(request, 'pockemon/pokemons.html',
                               {
                                   "title": "Names",
                                   "pokemons_names": pokemons_names
                               }))


def status(request):
    return HttpResponse('OK')
