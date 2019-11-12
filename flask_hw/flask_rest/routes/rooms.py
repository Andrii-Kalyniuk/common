from flask import request
from flask_restful import Resource, fields, reqparse

from db.db import DB
from models import Room

parser = reqparse.RequestParser()
parser.add_argument('status')


class Rooms(Resource):
    room_structure = {
        "number": fields.Integer,
        "level": fields.String,
        "status": fields.String,
        "price": fields.Float,
        "id": fields.String
    }

    def get(self, id_=None):
        room_all = [room.__dict__ for room in DB['rooms']]
        args = parser.parse_args()
        print(20 * '*', id_)
        print(20 * '*', args)
        if id_:
            room = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room:
                return room[0].__dict__
            else:
                return {"message": "room not found"}, 404
        else:
            if args['status']:
                return list(filter(lambda r: args['status'] == r['status'],
                                   room_all))
        return room_all

    def post(self):
        data = request.json
        DB['rooms'].append(Room(data.get('number'),
                                data.get('level'),
                                data.get('status'),
                                data.get('price')))
        return {"message": "room was added"}, 201

    def patch(self, id_):
        args = request.json
        print(20 * '*', id_)
        print(20 * '*', args)
        if id_:
            room_to_update = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room_to_update:
                if args:
                    upd_here = DB['rooms'].index(room_to_update[0])
                    updating_room = DB['rooms'][upd_here]
                    updating_room.number = args.get('number',
                                                    updating_room.number)
                    updating_room.level = args.get('level',
                                                   updating_room.level)
                    updating_room.status = args.get('status',
                                                    updating_room.status)
                    updating_room.price = args.get('price',
                                                   updating_room.price)
                    return {"message": "room was updated"}
                else:
                    return {"message": "nothing to update with"}, 404
            return {"message": "room was not found"}, 404

    def delete(self, id_=None):
        if id_:
            room_to_del = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room_to_del:
                DB['rooms'].remove(room_to_del[0])
                return {"message": "room was deleted"}
            return {"message": "room was not found"}, 404

