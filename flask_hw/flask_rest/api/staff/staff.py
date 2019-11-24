import logging

from flask import request
from flask_restful import marshal_with, Resource

from api.staff.staff_parsers import data_valid_for, data_valid_for_staff_room
from api.staff.structure import staff_structure
from db import Staff, db, Rooms

logging.basicConfig(level=logging.DEBUG)


class StaffRes(Resource):

    @marshal_with(staff_structure)
    def get(self, passport_id=None):
        staff_all = Staff.query.all()
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        args = data_valid_for('GET')
        logging.debug(staff_all)
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            staff = Staff.query.get(passport_id)
            if staff:
                return staff, header
            else:
                # how to display message instead of Staff structure here?
                return {"message": "staff not found"}, 404, header
        else:
            if args['name']:
                staff = Staff.query.filter_by(name=args['name']).all()
                return staff, header
            # add if name not found?
        return staff_all, header

    def post(self):
        data = data_valid_for('POST')
        logging.debug(data)
        if isinstance(data, dict):
            if not Staff.query.get(data['passport_id']):
                new_staff = Staff(**data)
                db.session.add(new_staff)
                db.session.commit()
                location = {
                    "Location":
                        f'/api/v0.1/staff/{str(new_staff.passport_id)}'
                }
                return {"message": "staff was added successfully"}, \
                       201, location
            msg = f"passport_id {data['passport_id']} already exists"
            return {"message": msg}, 400
        return {"message": "not enough arguments to add staff",
                "missing args": data}, 400

    def put(self, passport_id=None):
        args = data_valid_for('PUT')
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            staff = Staff.query.get(passport_id)
            if staff:
                if isinstance(args, dict):
                    if args['passport_id'] != passport_id \
                            and Staff.query.get(args['passport_id']):
                        msg = "passport_id " \
                              f"{args['passport_id']} already exists"
                        return {"message": msg}, 400
                    else:
                        staff.passport_id = args['passport_id']
                        staff.name = args['name']
                        staff.position = args['position']
                        staff.salary = args['salary']
                        db.session.commit()
                        return {}, 204
                else:
                    return {"message": "not enough arguments to update",
                            "missing args": args}, 400
            else:
                return {"message": "staff not found"}, 404
        return {"message": "staff passport_id not specified"}, 400

    def patch(self, passport_id=None):
        data = request.json
        logging.debug(passport_id)
        logging.debug(data)
        if passport_id:
            staff = Staff.query.get(passport_id)
            if staff:
                if data:
                    if data.get('passport_id') != passport_id and \
                            Staff.query.get(data.get('passport_id')):
                        msg = "passport_id" \
                              f" {data['passport_id']} already exists"
                        return {"message": msg}, 400
                    else:
                        staff.passport_id = data.get('passport_id',
                                                     staff.passport_id)
                        staff.name = data.get('name', staff.name)
                        staff.position = data.get('position', staff.position)
                        staff.salary = data.get('salary', staff.salary)
                        db.session.commit()
                    return {"message": "staff was updated"}
                else:
                    return {"message": "nothing to update with"}, 400
            return {"message": "staff was not found"}, 404
        return {"message": "staff passport_id not specified"}, 400

    def delete(self, passport_id=None):
        if passport_id:
            staff = Staff.query.get(passport_id)
            if staff:
                db.session.delete(staff)
                db.session.commit()
                return {"message": "staff was deleted"}, 204
            return {"message": "staff was not found"}, 404
        return {"message": "staff passport_id not specified"}, 400


class StaffRooms(Resource):

    @marshal_with(staff_structure)
    def get(self):
        data = data_valid_for_staff_room('GET')
        staff_by_name = Staff.query.filter_by(name=data['name']).all()
        return staff_by_name

    def post(self):
        data = data_valid_for_staff_room('POST')
        staff_name = data.get('staff_name')
        room_number = data.get('room_number')
        staff = Staff.query.filter_by(name=staff_name).first()
        room = Rooms.query.filter_by(number=room_number).first()
        logging.debug(staff.passport_id)
        room.serve_by.append(staff)
        db.session.commit()
        logging.debug(room.serve_by)
        msg_content = f'{staff_name} added to the room #{room_number} service'
        return {"message": msg_content}
