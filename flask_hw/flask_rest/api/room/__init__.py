from flask import Blueprint
from flask_restful import Api

from api.room.rooms import RoomsRes

rooms_bp = Blueprint('rooms', __name__)
rooms_api = Api(rooms_bp)
rooms_api.add_resource(RoomsRes, '/api/v0.1/rooms', '/api/v0.1/rooms/<int:number>')
