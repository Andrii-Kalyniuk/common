import json

from flask import request
from flask_restful import Resource, marshal_with, current_app

from db import db

from one_to_many_example.structures import street_structure, house_structure
from models.one_to_many_example import Street, House


class StreetView(Resource):
    @marshal_with(street_structure)
    def get(self):
        return Street.query.all()

    def post(self):
        data = json.loads(request.data)

        try:
            house_id = data.pop("house_id")
            house = House.query.get(house_id)
            data['houses'] = house
        except KeyError:
            current_app.logger.info("House was not created")

        street = Street(**data)
        db.session.add(street)
        db.session.commit()
        return "Successfully added the new Street"


class HouseView(Resource):
    @marshal_with(house_structure)
    def get(self):
        return House.query.all()

    def post(self):
        data = json.loads(request.data)
        house_obj = House(**data)
        db.session.add(house_obj)
        db.session.commit()
        return "Successfully added the new House"


class StreetHouses(Resource):
    @marshal_with(house_structure)
    def get(self, value):
        street = Street.query.get(value)
        return street.houses
