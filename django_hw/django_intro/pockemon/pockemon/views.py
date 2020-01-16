import requests
from django.http import HttpResponse
from django.shortcuts import render
from .settings import POCKEMON_URL


def get_pokemons():
    return requests.get(f'{POCKEMON_URL}/type/3').json()


def index(request):
    context = {"title": "Home", "link_text": "Show me all pokemons"}
    return HttpResponse(render(request, 'pockemon/index.html', context))


def show_all_names(request):
    pokemons_names = [p['pokemon']['name'] for p in get_pokemons()['pokemon']]
    context = {"title": "Names", "pokemons_names": pokemons_names}
    return HttpResponse(render(request, 'pockemon/pokemons.html', context))


def status(request):
    return HttpResponse('OK')
