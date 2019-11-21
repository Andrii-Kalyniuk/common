from flask_restful import Resource, marshal_with, request
import json
from api.films.structures import films_structure
from db import Films, db


class FilmsResource(Resource):
    method_decorators = [marshal_with(films_structure)]

    def get(self):
        return Films.query.all()

    def post(self):
        body = json.loads(request.data)
        film = Films(**body)
        db.session.add(film)
        db.session.commit()

        return Films.query.all(), 201

    def put(self, value):
        body = json.loads(request.data)
        film = Films.query.get(value)
        film.name = body.get('name')
        db.session.commit()
        return Films.query.all()

    def delete(self, value):
        film = Films.query.get(value)
        db.session.delete(film)
        db.session.commit()
        return Films.query.all()
