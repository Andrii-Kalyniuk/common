import json

from flask import Response, request
from flask_restful import Resource

from src.infrasturcture import DB
from src.model import City


class CityView(Resource):
    def get(self):
        data = [{'name': city.name,'id': city.id}
                for city in DB['cities']]
        data = json.dumps(data)
        return Response(data, status=200)

    def post(self):
        data = request.json
        DB['cities'].append(City(data['name']))
        return Response(status=200)

    def delete(self, id):
        data = request.json
        print(data)
        for city in DB['cities']:
            if city['id'] == data['id']:
                del city
        return Response(status=200)
