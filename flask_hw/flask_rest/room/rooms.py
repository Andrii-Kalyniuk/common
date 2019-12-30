import logging

from flask_restful import Resource

from db.db import DB
from models import Room
from room.room_parsers import data_valid_for

logging.basicConfig(level=logging.DEBUG)


def is_number_exist(args, number, db):
    return args.get('number') != number and \
           list(filter(lambda r: args.get('number') == r.number, db))


class RoomsRes(Resource):

    def get(self, number=None):
        rooms_all = [room.serialize() for room in DB['rooms']]
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        args = data_valid_for('GET')
        logging.debug(rooms_all)
        logging.debug(number)
        logging.debug(args)
        if number:
            rooms = list(filter(lambda r: number == r.number, DB['rooms']))
            if rooms:
                return rooms[0].serialize(), header
            return {"message": "room not found"}, 404, header
        else:
            if args['status']:
                return list(filter(lambda r: args['status'] == r['status'],
                                   rooms_all)), header
        return rooms_all, header

    def post(self):
        data = data_valid_for('POST')
        logging.debug(data)
        rooms_already_exist = list(filter(lambda r: data['number'] == r.number,
                                          DB['rooms']))
        if not rooms_already_exist:
            DB['rooms'].append(Room(**data))
            new_number = str(DB['rooms'][-1].number)
            location = {"Location": f'/api/v0.1/rooms/{new_number}'}
            return {"message": "room was added successfully"}, 201, location
        msg = f"room with number {data['number']} already exists"
        return {"message": msg}, 400

    def put(self, number=None):
        args = data_valid_for('PUT')
        logging.debug(number)
        logging.debug(args)
        if number:
            room = list(filter(lambda r: number == r.number, DB['rooms']))
            if room:
                # if new room number already in DB
                if is_number_exist(args, number, DB['rooms']):
                    msg = f"number {args['number']} already exists"
                    return {"message": msg}, 400
                room[0].number = args['number']
                room[0].level = args['level']
                room[0].status = args['status']
                room[0].price = args['price']
                return {"message": "room was updated successfully",
                        "room": room[0].serialize()}, 200
            return {"message": "room not found"}, 404
        return {"message": "room number not specified"}, 404

    def patch(self, number=None):
        args = data_valid_for('PATCH')
        logging.debug(number)
        logging.debug(args)
        if number:
            room_to_update = list(filter(lambda r: number == r.number,
                                         DB['rooms']))
            if room_to_update:
                if args:
                    if is_number_exist(args, number, DB['rooms']):
                        msg = f"number {args['number']} already exists"
                        return {"message": msg}, 400
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
                return {"message": "nothing to update with"}
            return {"message": "room was not found"}, 404
        return {"message": "room number not specified"}, 400

    def delete(self, number=None):
        if number:
            room_to_del = list(filter(lambda r: number == r.number,
                                      DB['rooms']))
            if room_to_del:
                DB['rooms'].remove(room_to_del[0])
                return {"message": "room was deleted"}, 204
            return {"message": "room was not found"}, 404
        return {"message": "room number not specified"}, 400
