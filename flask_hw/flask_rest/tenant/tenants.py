import logging

from flask import request
from flask_restful import Resource, reqparse, fields, marshal

from db.db import DB
from models import Tenant

logging.basicConfig(level=logging.DEBUG)
parser = reqparse.RequestParser()


class TenantsRes(Resource):

    address_structure = {
        "city": fields.String,
        "street": fields.String
    }
    tenant_structure = {
        "name": fields.String,
        "age": fields.String,
        "sex": fields.String,
        "address": fields.Nested(address_structure),
        "room_number": fields.Integer,
        "passport_id": fields.String
    }

    def get(self, id_=None):
        tenants_all = [marshal(tenant, self.tenant_structure)
                       for tenant in DB['tenants']]
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        parser.add_argument('name')
        args = parser.parse_args(strict=True)
        logging.debug(id_)
        logging.debug(args)
        if id_:
            tenant = list(filter(lambda t: id_ == t.passport_id,
                                 DB['tenants']))
            if tenant:
                # return marshal(tenant[0], self.tenant_structure), header
                return tenant[0].__dict__, header
            else:
                return {"message": "tenant not found"}, 404, header
        else:
            if args['name']:
                return list(filter(lambda r: args['name'] == r['name'],
                                   tenants_all)), header
        return tenants_all, header

    def post(self):
        data = request.json
        if data:
            DB['tenants'].append(Tenant(data.get('name'),
                                        data.get('age'),
                                        data.get('sex'),
                                        data.get('address'),
                                        data.get('room_number')))
            location = {"Location": '/api/v0.1/tenants/'
                                    + DB['tenants'][-1].passport_id}
            return {"message": "tenant was add successfully"}, 201, location
        return {"message": "nothing to add"}, 404

    def put(self, id_=None):
        args = request.json
        logging.debug(id_)
        logging.debug(args)
        if id_:
            tenant = list(filter(lambda t: id_ == t.passport_id,
                                 DB['tenants']))
            if tenant:
                if all(args.values()):
                    tenant[0].name = args['name']
                    tenant[0].age = args['age']
                    tenant[0].sex = args['sex']
                    tenant[0].address = args['address']
                    tenant[0].room_number = args['room_number']
                    return {}, 204
                else:
                    return {"message": "not enough arguments to update"}
            else:
                return {"message": "tenant not found"}, 404
        return {"message": "id not specified"}, 404

    def patch(self, id_=None):
        args = request.json
        logging.debug(id_)
        logging.debug(args)
        if id_:
            tenant_to_update = list(filter(lambda t: id_ == t.passport_id,
                                           DB['tenants']))
            if tenant_to_update:
                if args:
                    upd_here = DB['tenants'].index(tenant_to_update[0])
                    tenant = DB['tenants'][upd_here]
                    tenant.name = args.get('name',tenant.name)
                    tenant.age = args.get('age', tenant.age)
                    tenant.sex = args.get('sex', tenant.sex)
                    tenant.address = args.get('address', tenant.address)
                    tenant.room_number = args.get('room_number',
                                                  tenant.room_number)
                    return {"message": "tenant was updated"}
                else:
                    return {"message": "nothing to update with"}, 404
            return {"message": "tenant was not found"}, 404

    def delete(self, id_=None):
        if id_:
            tenant_to_del = list(filter(lambda t: id_ == t.passport_id,
                                        DB['tenants']))
            if tenant_to_del:
                DB['tenants'].remove(tenant_to_del[0])
                return {"message": "tenant was deleted"}
            return {"message": "tenant was not found"}, 404
        return {"message": "id not specified"}, 404
