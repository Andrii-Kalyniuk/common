from flask_restful import Resource, reqparse, fields

from db.db import DB

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('passport_id')
parser.add_argument('sex')
parser.add_argument('address')
parser.add_argument('room_number')


class Tenants(Resource):
    tenants_structure = {
        "name": fields.String,
        "age": fields.String,
        "sex": fields.String,
        "address": fields.String,
        "room_number": fields.Integer,
        "passport_id": fields.String,
    }

    def get(self, id_=None):
        tenants_all = [tenant.__dict__ for tenant in DB['tenants']]
        args = parser.parse_args()
        print(20 * '*', id_)
        print(20 * '*', args)
        if id_:
            tenant = list(filter(lambda t: id_ == t.passport_id,
                                 DB['tenants']))
            if tenant:
                return tenant[0].__dict__
            else:
                return {"message": "tenant not found"}, 404
        else:
            if args['name']:
                return list(filter(lambda r: args['name'] == r['name'],
                                   tenants_all))
        return tenants_all

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
