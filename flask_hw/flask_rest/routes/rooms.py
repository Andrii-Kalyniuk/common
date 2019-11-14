import logging

from flask import request
from flask_restful import Resource, reqparse

from db.db import DB
from models import Room

logging.basicConfig(level=logging.DEBUG)
parser = reqparse.RequestParser()


class Rooms(Resource):

    def get(self, id_=None):
        room_all = [room.serialize() for room in DB['rooms']]
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        parser.add_argument('status')
        args = parser.parse_args(strict=True)
        logging.debug(id_)
        logging.debug(args)
        if id_:
            room = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room:
                return room[0].serialize(), header
            else:
                return {"message": "room not found"}, 404, header
        else:
            if args['status']:
                return list(filter(lambda r: args['status'] == r['status'],
                                   room_all)), header
        return room_all, header

    def post(self):
        data = request.json
        if data:
            DB['rooms'].append(Room(data.get('number'),
                                    data.get('level'),
                                    data.get('status'),
                                    data.get('price')))
            location = {"Location": '/api/v0.1/rooms/'
                                    + DB['rooms'][-1].id}
            return {"message": "room was added successfully"}, 201, location
        return {"message": "nothing to add"}, 404

    def put(self, id_=None):
        parser.add_argument('number', type=int)
        parser.add_argument('level')
        parser.add_argument('status')
        parser.add_argument('price', type=float)
        args = parser.parse_args()
        logging.debug(id_)
        logging.debug(args)
        if id_:
            room = list(filter(lambda r: id_ == r.id, DB['rooms']))
            if room:
                if all(args.values()):
                    room[0].number = args['number']
                    room[0].level = args['level']
                    room[0].status = args['status']
                    room[0].price = args['price']
                    return {}, 204
                else:
                    return {"message": "not enough arguments to update"}
            else:
                return {"message": "room not found"}, 404
        return {"message": "id not specified"}, 404

    def patch(self, id_=None):
        args = request.json
        logging.debug(id_)
        logging.debug(args)
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
                return {"message": "room was deleted"}, 204
            return {"message": "room was not found"}, 404
        return {"message": "id not specified"}, 404
