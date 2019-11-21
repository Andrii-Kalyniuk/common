from flask_restful import Api
from flask import Blueprint

from api.films.resource import FilmsResource

films_blueprint = Blueprint("films", __name__)
films_api = Api(films_blueprint)

films_api.add_resource(FilmsResource, '/films', '/films/<value>')
