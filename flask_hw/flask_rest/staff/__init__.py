from flask import Blueprint
from flask_restful import Api

from staff.staff import StaffRes

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)
api.add_resource(StaffRes, '/api/v0.1/staff', '/api/v0.1/staff/<id_>')
