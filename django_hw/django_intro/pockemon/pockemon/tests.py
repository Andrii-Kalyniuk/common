from http import HTTPStatus

from django.test import TestCase
from django.test import Client

from django.urls import reverse


class StatusViewTests(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get(reverse('status'))
        assert response.status_code == HTTPStatus.OK

    def test_index_page(self):
        response = self.client.get(reverse('index'),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_data_returned_from_pokemon_API(self):
        pass

    def test_invalid_data_returned(self):
        pass
