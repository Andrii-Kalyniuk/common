from flask import request
from flask_restful import Resource, fields

from db.db import DB
from models import Room


class Rooms(Resource):
    room_structure = {
        "number": fields.Integer,
        "level": fields.String,
        "status": fields.String,
        "price": fields.Float,
        "id": fields.String
    }

    def get(self, room_id=None):
        if room_id:
            print(20*'*', room_id)
            room = list(filter(lambda r: room_id == r.id, DB['rooms']))
            if room:
                return room[0].__dict__, 200
        else:
            room_all = [room.__dict__ for room in DB['rooms']]
            return room_all, 200

    def post(self):
        data = request.json
        DB['rooms'].append(Room(data.get('number'),
                                data.get('level'),
                                data.get('status'),
                                data.get('price')))
        return {"message": "room added"}, 200
