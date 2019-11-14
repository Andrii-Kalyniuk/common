import logging

from flask import request
from flask_restful import Resource, reqparse

from db.db import DB
from models import Staff

logging.basicConfig(level=logging.DEBUG)
parser = reqparse.RequestParser()


class StaffRes(Resource):

    def get(self, id_=None):
        staff_all = [staff.__dict__ for staff in DB['staff']]
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        parser.add_argument('position')
        args = parser.parse_args(strict=True)
        logging.debug(id_)
        logging.debug(args)
        if id_:
            staff = list(filter(lambda s: id_ == s.passport_id, DB['staff']))
            if staff:
                return staff[0].__dict__, header
            else:
                return {"message": "staff not found"}, 404, header
        else:
            if args['position']:
                return list(filter(lambda r: args['position'] == r['position'],
                                   staff_all)), header
        return staff_all, header

    def post(self):
        parser.add_argument('name')
        parser.add_argument('position')
        parser.add_argument('salary', type=float)
        args = parser.parse_args(strict=True)
        logging.debug(args)
        if all(args.values()):
            DB['staff'].append(Staff(args['name'],
                                     args['position'],
                                     args['salary']))
            location = {"Location": '/api/v0.1/staff/'
                                    + DB['staff'][-1].passport_id}
            return {"message": "staff was added successfully"}, 201, location
        return {"message": "not enough arguments to add staff"}, 404

    def put(self, id_=None):
        parser.add_argument('name')
        parser.add_argument('position')
        parser.add_argument('salary', type=float)
        args = parser.parse_args(strict=True)
        logging.debug(id_)
        logging.debug(args)
        if id_:
            staff = list(filter(lambda s: id_ == s.passport_id, DB['staff']))
            if staff:
                if all(args.values()):
                    staff[0].name = args['name']
                    staff[0].position = args['position']
                    staff[0].salary = args['salary']
                    return {}, 204
                else:
                    return {"message": "not enough arguments to update"}
            else:
                return {"message": "staff not found"}, 404
        return {"message": "id not specified"}, 404

    def patch(self, id_=None):
        args = request.json
        logging.debug(id_)
        logging.debug(args)
        if id_:
            staff_to_update = list(filter(lambda s: id_ == s.passport_id,
                                          DB['staff']))
            if staff_to_update:
                if any(args.values()):
                    upd_here = DB['staff'].index(staff_to_update[0])
                    updating_staff = DB['staff'][upd_here]
                    updating_staff.name = args.get('name',
                                                   updating_staff.name)
                    updating_staff.position = args.get('position',
                                                       updating_staff.position)
                    updating_staff.salary = args.get('salary',
                                                     updating_staff.salary)
                    return {"message": "staff was updated"}
                else:
                    return {"message": "nothing to update with"}, 404
            return {"message": "staff was not found"}, 404

    def delete(self, id_=None):
        if id_:
            staff_to_del = list(filter(lambda s: id_ == s.passport_id,
                                       DB['staff']))
            if staff_to_del:
                DB['staff'].remove(staff_to_del[0])
                return {"message": "staff was deleted"}, 204
            return {"message": "staff was not found"}, 404
        return {"message": "id not specified"}, 404
