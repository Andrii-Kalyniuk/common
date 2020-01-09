from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests


POCKEMON_URL = 'https://pokeapi.co/api/v2/'

SIMPLE_TEMPLATE = """
<html>
<head>
    <title>Pokemon</title>
</head>
<body>
    <a href="/question">GIVE ME POKEMONS</a>
</body>
</html>
"""


def index(request):
    # return HttpResponse(SIMPLE_TEMPLATE)
    # loader.get_template('index.html')
    context = {'link_text': 'Take some pokemons'}
    return HttpResponse(render(request, 'pockemon/index.html', context))


def question(request):
    response = requests.get(f'{POCKEMON_URL}/type/3')
    return HttpResponse([f"{p['pokemon']['name']}<br />"
                         for p in response.json()['pokemon']])


def status(request):
    return HttpResponse('OK')
