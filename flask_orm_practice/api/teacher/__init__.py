from flask import Blueprint
from flask_restful import Api

from api.teacher.resources import TeacherResource

teacher_blueprint = Blueprint('teacher', __name__)
teacher_api = Api(teacher_blueprint)

teacher_api.add_resource(TeacherResource, '/teacher')
