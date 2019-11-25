import logging

from flask import request
from flask_restful import Resource, marshal_with

from db.db import DB
from models import Staff
from staff.staff_parsers import data_valid_for
from staff.staff_structure import staff_structure

logging.basicConfig(level=logging.DEBUG)


def is_passport_id_exist(args, passport_id, db):
    return args.get('passport_id') != passport_id and \
           list(filter(lambda t: args.get('passport_id') == t.passport_id, db))


class StaffRes(Resource):

    @marshal_with(staff_structure)
    def get(self, passport_id=None):
        staff_all = [staff for staff in DB['staff']]
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        args = data_valid_for('GET')
        logging.debug(staff_all)
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            staff = list(filter(lambda t: passport_id == t.passport_id,
                                DB['staff']))
            if staff:
                return staff[0], header
            else:
                return {"message": "staff not found"}, 404, header
        else:
            if args['name']:
                return list(filter(lambda r: args['name'] == r.name,
                                   staff_all)), header
        return staff_all, header

    def post(self):
        data = data_valid_for('POST')
        logging.debug(data)
        staff_already_exist = list(filter(lambda t: data['passport_id'] == t.passport_id,
                                          DB['staff']))
        if not staff_already_exist:
            DB['staff'].append(Staff(**data))
            new_passport_id = str(DB['staff'][-1].passport_id)
            location = {"Location": f'/api/v0.1/staff/{new_passport_id}'}
            return {"message": "staff was added successfully"}, 201, location
        msg = f"staff with passport_id {data['passport_id']} already exists"
        return {"message": msg}, 400

    def put(self, passport_id=None):
        args = data_valid_for('PUT')
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            staff = list(filter(lambda t: passport_id == t.passport_id,
                                DB['staff']))
            if staff:
                if is_passport_id_exist(args, passport_id, DB['staff']):
                    msg = f"passport_id {args['passport_id']} already exists"
                    return {"message": msg}, 400
                else:
                    staff[0].name = args['name']
                    staff[0].passport_id = args['passport_id']
                    staff[0].position = args['position']
                    staff[0].salary = args['salary']
                    return {}, 204
            else:
                return {"message": "staff not found"}, 404
        return {"message": "staff passport_id not specified"}, 404

    def patch(self, passport_id=None):
        args = request.json
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            staff_to_update = list(filter(
                lambda t: passport_id == t.passport_id, DB['staff']))
            if staff_to_update:
                if args:
                    if is_passport_id_exist(args, passport_id, DB['staff']):
                        msg = f"passport_id {args['passport_id']} already exists"
                        return {"message": msg}, 400
                    else:
                        upd_here = DB['staff'].index(staff_to_update[0])
                        updating_staff = DB['staff'][upd_here]
                        updating_staff.name = args.get(
                            'name', updating_staff.name)
                        updating_staff.passport_id = args.get(
                            'passport_id', updating_staff.passport_id)
                        updating_staff.position = args.get(
                            'position', updating_staff.position)
                        updating_staff.salary = args.get(
                            'salary', updating_staff.salary)
                        return {"message": "staff was updated"}
                return {"message": "nothing to update with"}
            return {"message": "staff was not found"}, 404
        return {"message": "staff number not specified"}, 400

    def delete(self, passport_id=None):
        if passport_id:
            staff_to_del = list(filter(lambda t: passport_id == t.passport_id,
                                         DB['staff']))
            if staff_to_del:
                DB['staff'].remove(staff_to_del[0])
                return {"message": "staff was deleted"}, 204
            return {"message": "staff was not found"}, 404
        return {"message": "staff number not specified"}, 400
