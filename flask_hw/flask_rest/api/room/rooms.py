import logging

from flask import request
from flask_restful import Resource, reqparse, marshal_with

from api.room.structure import room_structure
from db import Rooms, db


logging.basicConfig(level=logging.DEBUG)
parser = reqparse.RequestParser()


class RoomsRes(Resource):

    @marshal_with(room_structure)
    def get(self, number=None):
        room_all = Rooms.query.all()
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        parser.add_argument('status')
        args = parser.parse_args(strict=True)
        logging.debug(room_all)
        logging.debug(number)
        logging.debug(args)
        if number:
            room = Rooms.query.get(number)
            if room:
                return room, header
            else:
                return {"message": "room not found"}, 404, header
        else:
            if args['status']:
                return Rooms.query.filter_by(
                                status=args['status']).all(), header
        return room_all, header

    def post(self):
        data = request.json
        if all(data.values()):
            new_room = Rooms(**data)
            db.session.add(new_room)
            db.session.commit()
            location = {"Location": '/api/v0.1/rooms/' + str(new_room.number)}
            return {"message": "room was added successfully"}, 201, location
        return {"message": "not enough arguments to update"}, 404

    def put(self, number=None):
        parser.add_argument('number', type=int)
        parser.add_argument('level')
        parser.add_argument('status')
        parser.add_argument('price', type=float)
        args = parser.parse_args()
        logging.debug(number)
        logging.debug(args)
        if number:
            room = Rooms.query.get(number)
            if room:
                if all(args.values()):
                    room.number = args['number']
                    room.level = args['level']
                    room.status = args['status']
                    room.price = args['price']
                    db.session.commit()
                    return {}, 204
                else:
                    return {"message": "not enough arguments to update"}
            else:
                return {"message": "room not found"}, 404
        return {"message": "room number not specified"}, 404

    def patch(self, number=None):
        data = request.json
        logging.debug(number)
        logging.debug(data)
        if number:
            room = Rooms.query.get(number)
            if room:
                if data:
                    room.number = data.get('number', room.number)
                    room.level = data.get('level', room.level)
                    room.status = data.get('status', room.status)
                    room.price = data.get('price', room.price)
                    db.session.commit()
                    return {"message": "room was updated"}
                else:
                    return {"message": "nothing to update with"}, 404
            return {"message": "room was not found"}, 404
        return {"message": "room number not specified"}, 404

    def delete(self, number=None):
        if number:
            room = Rooms.query.get(number)
            if room:
                db.session.delete(room)
                db.session.commit()
                return {"message": "room was deleted"}, 204
            return {"message": "room was not found"}, 404
        return {"message": "room number not specified"}, 404
