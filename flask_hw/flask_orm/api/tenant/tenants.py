import logging

from flask_restful import Resource, marshal_with, marshal
from sqlalchemy.exc import SQLAlchemyError

from api.tenant.structure import tenant_structure
from api.tenant.tenant_parsers import data_valid_for

from db import Tenants, db

logging.basicConfig(level=logging.DEBUG)


class TenantsRes(Resource):

    @marshal_with(tenant_structure)
    def get(self, passport_id=None):
        tenants_all = Tenants.query.all()
        header = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "Pragma": "no-cache"
        }
        args = data_valid_for('GET')
        logging.debug(tenants_all)
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            tenant = Tenants.query.get_or_404(passport_id,
                                              description="tenant not found")
            if tenant:
                return tenant, header
        else:
            if args['name']:
                tenants = Tenants.query.filter_by(name=args['name']).all()
                # FIXME: if name not found just return empty list
                return tenants, header
        return tenants_all, header

    def post(self):
        data = data_valid_for('POST')
        logging.debug(data)
        if isinstance(data, dict):
            if not Tenants.query.get(data['passport_id']):
                new_tenant = Tenants(**data)
                db.session.add(new_tenant)
                # FIXME: what if tenant was not saved?
                try:
                    db.session.commit()
                except SQLAlchemyError:
                    return {"message": "could not save to database, try later"}
                location = {
                    "Location":
                        f'/api/v0.1/tenants/{str(new_tenant.passport_id)}'
                }
                # FIXME: return tenant data instead of message
                return {"message": "tenant was added successfully",
                        "room": marshal(new_tenant, tenant_structure)}, \
                       201, location
            msg = f"passport_id {data['passport_id']} already exists"
            return {"message": msg}, 400
        return {"message": "not enough arguments to add tenant",
                "missing args": data}, 400

    def put(self, passport_id=None):
        args = data_valid_for('PUT')
        logging.debug(passport_id)
        logging.debug(args)
        if passport_id:
            tenant = Tenants.query.get(passport_id)
            if tenant:
                if isinstance(args, dict):
                    if args['passport_id'] != passport_id \
                            and Tenants.query.get(args['passport_id']):
                        msg = "passport_id " \
                              f"{args['passport_id']} already exists"
                        return {"message": msg}, 400
                    else:
                        tenant.passport_id = args['passport_id']
                        tenant.name = args['name']
                        tenant.age = args['age']
                        tenant.sex = args['sex']
                        tenant.city = args['city']
                        tenant.address = args['address']
                        # FIXME: what if tenant was not saved?
                        try:
                            db.session.commit()
                        except SQLAlchemyError:
                            return {"message": "could not save to database,"
                                               " try later"}
                        return {"message": "tenant was updated successfully",
                                "tenant": marshal(tenant, tenant_structure)}, \
                               200
                else:
                    return {"message": "not enough arguments to update",
                            "missing args": args}, 400
            else:
                return {"message": "tenant not found"}, 404
        return {"message": "tenant passport_id not specified"}, 400

    def patch(self, passport_id=None):
        data = data_valid_for('PATCH')
        logging.debug(passport_id)
        logging.debug(data)
        if passport_id:
            tenant = Tenants.query.get(passport_id)
            if tenant:
                if data:
                    if data.get('passport_id') != passport_id \
                            and Tenants.query.get(data.get('passport_id')):
                        msg = "passport_id" \
                              f" {data['passport_id']} already exists"
                        return {"message": msg}, 400
                    else:
                        tenant.passport_id = data.get('passport_id',
                                                      tenant.passport_id)
                        tenant.name = data.get('name', tenant.name)
                        tenant.age = data.get('age', tenant.age)
                        tenant.sex = data.get('sex', tenant.sex)
                        tenant.city = data.get('city', tenant.city)
                        tenant.address = data.get('address', tenant.address)
                        # FIXME: what if tenant was not saved?
                        try:
                            db.session.commit()
                        except SQLAlchemyError:
                            return {"message": "could not save to database,"
                                               " try later"}
                    return {"message": "tenant was updated successfully",
                            "tenant": marshal(tenant, tenant_structure)}
                else:
                    return {"message": "nothing to update with"}, 400
            return {"message": "tenant was not found"}, 404
        return {"message": "tenant passport_id not specified"}, 400

    def delete(self, passport_id=None):
        if passport_id:
            tenant = Tenants.query.get(passport_id)
            if tenant:
                db.session.delete(tenant)
                # FIXME: what if tenant was not deleted?
                try:
                    db.session.commit()
                except SQLAlchemyError:
                    return {"message": "could not save to database,"
                                       " try later"}
                return {"message": "tenant was deleted"}, 204
            return {"message": "tenant was not found"}, 404
        return {"message": "tenant passport_id not specified"}, 400
