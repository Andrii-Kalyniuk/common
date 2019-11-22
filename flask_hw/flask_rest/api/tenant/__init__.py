from flask import Blueprint
from flask_restful import Api

from api.tenant.tenants import TenantsRes

tenants_bp = Blueprint('tenants', __name__)
api = Api(tenants_bp)
api.add_resource(TenantsRes, '/api/v0.1/tenants',
                 '/api/v0.1/tenants/<passport_id>')
