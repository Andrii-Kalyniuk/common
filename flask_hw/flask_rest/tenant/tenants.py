import logging

from flask_restful import Resource, marshal_with, marshal

from db.db import DB
from models import Tenant
from tenant.tenant_parsers import data_valid_for
from tenant.tenant_structure import tenant_structure

logging.basicConfig(level=logging.DEBUG)


def is_passport_id_exist(args, passport_id, db):
    return args.get('passport_id') != passport_id and \
           list(filter(lambda t: args.get('passport_id') == t.passport_id, db))


class TenantsRes(Resource):

    @marshal_with(tenant_structure)
    def get(self, passport_id=None):
        tenants_all = [tenant for tenant in DB['tenants']]
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        args = data_valid_for('GET')
        logging.debug(tenants_all)
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            tenants = list(filter(lambda t: passport_id == t.passport_id,
                                  DB['tenants']))
            if tenants:
                return tenants[0], header
            return {"message": "tenant not found"}, 404, header
        else:
            if args['name']:
                return list(filter(lambda r: args['name'] == r.name,
                                   tenants_all)), header
        return tenants_all, header

    def post(self):
        data = data_valid_for('POST')
        logging.debug(data)
        tenants_already_exist = list(filter(lambda t: data['passport_id'] == t.passport_id,
                                            DB['tenants']))
        if not tenants_already_exist:
            DB['tenants'].append(Tenant(**data))
            new_passport_id = str(DB['tenants'][-1].passport_id)
            location = {"Location": f'/api/v0.1/tenants/{new_passport_id}'}
            return {"message": "tenant was added successfully"}, 201, location
        msg = f"tenant with passport_id {data['passport_id']} already exists"
        return {"message": msg}, 400

    def put(self, passport_id=None):
        args = data_valid_for('PUT')
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            tenants = list(filter(lambda t: passport_id == t.passport_id,
                                  DB['tenants']))
            if tenants:
                if is_passport_id_exist(args, passport_id, DB['tenants']):
                    msg = f"passport_id {args['passport_id']} already exists"
                    return {"message": msg}, 400
                tenants[0].name = args['name']
                tenants[0].passport_id = args['passport_id']
                tenants[0].age = args['age']
                tenants[0].sex = args['sex']
                tenants[0].address = args['address']
                tenants[0].room_number = args['room_number']
                return {"message": "tenant was updated successfully",
                        "tenant": marshal(tenants[0], tenant_structure)}, 200
            return {"message": "tenant not found"}, 404
        return {"message": "tenant passport_id not specified"}, 404

    def patch(self, passport_id=None):
        args = data_valid_for('PATCH')
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            tenants_to_update = list(filter(
                lambda t: passport_id == t.passport_id, DB['tenants']))
            if tenants_to_update:
                if args:
                    if is_passport_id_exist(args, passport_id, DB['tenants']):
                        msg = f"passport_id {args['passport_id']} already exists"
                        return {"message": msg}, 400
                    upd_here = DB['tenants'].index(tenants_to_update[0])
                    updating_tenant = DB['tenants'][upd_here]
                    updating_tenant.name = args.get('name',
                                                    updating_tenant.name)
                    updating_tenant.passport_id = args.get(
                        'passport_id', updating_tenant.passport_id)
                    updating_tenant.age = args.get('age',
                                                   updating_tenant.age)
                    updating_tenant.sex = args.get('sex',
                                                   updating_tenant.sex)
                    updating_tenant.address = args.get('address',
                                                       updating_tenant.address)
                    updating_tenant.room_number = args.get(
                        'room_number', updating_tenant.room_number)
                    return {"message": "tenant was updated"}
                return {"message": "nothing to update with"}
            return {"message": "tenant was not found"}, 404
        return {"message": "tenant number not specified"}, 400

    def delete(self, passport_id=None):
        if passport_id:
            tenants_to_del = list(filter(lambda t: passport_id == t.passport_id,
                                         DB['tenants']))
            if tenants_to_del:
                DB['tenants'].remove(tenants_to_del[0])
                return {"message": "tenant was deleted"}, 204
            return {"message": "tenant was not found"}, 404
        return {"message": "tenant number not specified"}, 400
