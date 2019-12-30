from flask import Blueprint
from flask_restful import Api

from staff.staff import StaffRes

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp, catch_all_404s=True)
api.add_resource(StaffRes, '/api/v0.1/staff', '/api/v0.1/staff/<passport_id>')
