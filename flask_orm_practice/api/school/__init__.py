from flask import Blueprint
from flask_restful import Api

from api.school.resources import SchoolResource

school_blueprint = Blueprint('school', __name__)
school_api = Api(school_blueprint)

school_api.add_resource(SchoolResource, '/school')
