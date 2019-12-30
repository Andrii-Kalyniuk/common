import json
from unittest import TestCase
from app import create_app
from db import db, Films

app = create_app("TEST")


class TestFilms(TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        film = Films(name="The Shawshank Redemption")
        db.session.add(film)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_films(self):
        resp = app.test_client().get('/films')
        expected_result = [{"id": 1, "name": "The Shawshank Redemption"}]
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json, expected_result)

    def test_post_films(self):
        expected_result = [{"id": 1, "name": "The Shawshank Redemption"},
                           {"id": 2, "name": "Joker"}]
        data = json.dumps({"name": "Joker"})
        resp = app.test_client().post('/films', data=data, content_type='application/json')
        self.assertEquals(resp.status_code, 201)
        self.assertEquals(resp.json, expected_result)

    def test_update_films(self):
        expected_result = [{"id": 1, "name": "Avengers"}]
        data = json.dumps({"name": "Avengers"})
        resp = app.test_client().put('/films/1', data=data, content_type='application/json')

        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json, expected_result)

    def test_delete_films(self):
        expected_result = []
        resp = app.test_client().delete('/films/1')

        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json, expected_result)
