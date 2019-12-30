from flask import Blueprint
from flask_restful import Api

from api.students.resources import StudentResource

student_blueprint = Blueprint('student', __name__)
student_api = Api(student_blueprint)

student_api.add_resource(StudentResource, '/student')
