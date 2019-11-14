from flask import Blueprint
from flask_restful import Api

from room.rooms import RoomsRes

rooms_bp = Blueprint('rooms', __name__)
api = Api(rooms_bp)
api.add_resource(RoomsRes, '/api/v0.1/rooms', '/api/v0.1/rooms/<id_>')
