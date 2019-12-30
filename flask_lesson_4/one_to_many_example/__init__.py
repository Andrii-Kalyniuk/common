from flask import Blueprint
from flask_restful import Api

from one_to_many_example.routes import StreetView, HouseView, StreetHouses

one_to_many = Blueprint("one_to_many", __name__)
api_one_to_many = Api(one_to_many)

api_one_to_many.add_resource(StreetView, "/street")
api_one_to_many.add_resource(HouseView, "/house")
api_one_to_many.add_resource(StreetHouses, "/street/<value>")
