import logging

from flask import request
from flask_restful import Resource, marshal_with

from api.room.room_parsers import data_valid_for
from api.room.structure import room_structure
from db import Rooms, db

logging.basicConfig(level=logging.DEBUG)


class RoomsRes(Resource):

    @marshal_with(room_structure)
    def get(self, number=None):
        room_all = Rooms.query.all()
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        args = data_valid_for('GET')
        logging.debug(room_all)
        logging.debug(number)
        logging.debug(args)
        if number:
            room = Rooms.query.get(number)
            if room:
                return room, header
            else:
                # todo: how to display message instead of Rooms
                #  structure with nulls?
                return {"message": "room not found"}, 404, header
        else:
            if args['status']:
                rooms = Rooms.query.filter_by(status=args['status']).all()
                return rooms, header
            # todo: add if status not found?
        return room_all, header

    def post(self):
        data = data_valid_for('POST')
        logging.debug(data)
        if not Rooms.query.get(data['number']):
            new_room = Rooms(**data)
            db.session.add(new_room)
            db.session.commit()
            location = {
                "Location": f'/api/v0.1/rooms/{str(new_room.number)}'
            }
            return {"message": "room was added successfully"}, \
                   201, location
        msg = f"number {data['number']} already exists"
        return {"message": msg}, 400

    def put(self, number=None):
        args = data_valid_for('PUT')
        logging.debug(number)
        logging.debug(args)
        if number:
            room = Rooms.query.get(number)
            if room:
                if args['number'] != number \
                        and Rooms.query.get(args['number']):
                    msg = f"number {args['number']} already exists"
                    return {"message": msg}, 400
                else:
                    # why it's not work?
                    # room = Rooms(**args)
                    room.number = args['number']
                    room.level = args['level']
                    room.status = args['status']
                    room.price = args['price']
                    # todo: what if tenant_id updated
                    #  with value that not in db yet?
                    room.tenant_id = args['tenant_id']
                    db.session.commit()
                    return {}, 204
            else:
                return {"message": "room not found"}, 404
        return {"message": "room number not specified"}, 400

    def patch(self, number=None):
        data = request.json
        logging.debug(number)
        logging.debug(data)
        if number:
            room = Rooms.query.get(number)
            if room:
                if data:
                    if data.get('number') != number \
                            and Rooms.query.get(data.get('number')):
                        msg = f"number {data['number']} already exists"
                        return {"message": msg}, 400
                    else:
                        room.number = data.get('number', room.number)
                        room.level = data.get('level', room.level)
                        room.status = data.get('status', room.status)
                        room.price = data.get('price', room.price)
                        # todo: what if tenant_id updated
                        #  with value that not in db yet?
                        room.tenant_id = data.get('tenant_id', room.tenant_id)
                        db.session.commit()
                    return {"message": "room was updated"}
                else:
                    return {"message": "nothing to update with"}, 400
            return {"message": "room was not found"}, 404
        return {"message": "room number not specified"}, 400

    def delete(self, number=None):
        if number:
            room = Rooms.query.get(number)
            if room:
                db.session.delete(room)
                db.session.commit()
                return {"message": "room was deleted"}, 204
            return {"message": "room was not found"}, 404
        return {"message": "room number not specified"}, 400
