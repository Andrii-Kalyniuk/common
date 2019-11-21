from flask_restful import Api
from flask import Blueprint

from api.studios.resource import StudiosResource

studios_blueprint = Blueprint("studios", __name__)
studios_api = Api(studios_blueprint)

studios_api.add_resource(StudiosResource, '/studios')
