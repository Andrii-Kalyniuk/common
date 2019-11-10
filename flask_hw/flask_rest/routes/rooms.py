import json

from flask import Response
from flask_restful import Resource

from db.db import DB


class Rooms(Resource):
    def get(self):
        room_all = [
            {
                'number': room.number,
                'level': room.level,
                'status': room.status,
                'price': room.price,
                'id': room.id
            }
            for room in DB['rooms']]
        resp = json.dumps(room_all)
        return resp, 200
