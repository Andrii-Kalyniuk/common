from flask import Blueprint
from flask_restful import Api

from api.diary.resources import DiaryResource

diary_blueprint = Blueprint('diary', __name__)
diary_api = Api(diary_blueprint)

diary_api.add_resource(DiaryResource, '/diary')
