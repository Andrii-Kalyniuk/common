from flask import request
from flask_restful import Resource, fields, reqparse

from db.db import DB
from models import Room

parser = reqparse.RequestParser()
parser.add_argument('number')
parser.add_argument('level')
parser.add_argument('status')
parser.add_argument('price')
# parser.add_argument('id')

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
        print(20*'*', id_)
        print(20*'*', args)
        if id_:
            room = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room:
                return room[0].__dict__, 200
        else:
            if args['status']:
                return list(filter(lambda r: args['status'] == r['status'],
                                   room_all)), args
        return room_all, 200

    def post(self):
        data = request.json
        DB['rooms'].append(Room(data.get('number'),
                                data.get('level'),
                                data.get('status'),
                                data.get('price')))
        return {"message": "room was added"}, 201

    def patch(self, id_):
        args = request.json
        print(20*'*', id_)
        print(20*'*', args)
        if id_:
            room_to_update = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room_to_update
                if args:
                    upd_here = DB['rooms'].index(room_to_update[0])
                    DB['rooms'][upd_here].number = args.get('number', DB['rooms'][upd_here].number)
                    DB['rooms'][upd_here].level = args.get('level', DB['rooms'][upd_here].level)
                    DB['rooms'][upd_here].status = args.get('status', DB['rooms'][upd_here].status)
                    DB['rooms'][upd_here].price = args.get('price', DB['rooms'][upd_here].price)
                    return {"message": "room was updated"}
                else:

            return {"message": "room was not found"}, 404

    def put(self):
        pass

    def delete(self, id_=None):
        if id_:
            room_to_del = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room_to_del:
                DB['rooms'].remove(room_to_del[0])
                return {"message": "room was deleted"}
            return {"message": "room was not found"}, 404
