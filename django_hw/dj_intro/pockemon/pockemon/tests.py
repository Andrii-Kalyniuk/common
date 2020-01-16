import requests
from django.test import TestCase
from django.test import Client

from django.urls import reverse

from .settings import POCKEMON_URL
from .views import get_pokemons


class StatusViewTests(TestCase):
    client = Client()
    urls_4_test = ('status', 'index', 'show_all_names')

    def test_views_status(self):
        for url in self.urls_4_test:
            with self.subTest(url=url):
                response = self.client.get(reverse(url))
                assert response.status_code == 200


class ApiDataValidationTests(TestCase):

    def test_data_returned_from_poke_api(self):
        response = requests.get(f'{POCKEMON_URL}/type/3')
        assert response.status_code == 200

    def test_invalid_data_returned(self):

        def is_keys_valid(keys):
            obligatory_keys = ('name', 'url')
            for key in keys:
                if key not in obligatory_keys:
                    return False
            return True

        pokemons_json = get_pokemons()
        assert isinstance(pokemons_json, dict)
        pokemons_list = [p['pokemon'] for p in pokemons_json['pokemon']]
        actual_keys = [is_keys_valid(p.keys()) for p in pokemons_list]
        assert all(actual_keys) is True
