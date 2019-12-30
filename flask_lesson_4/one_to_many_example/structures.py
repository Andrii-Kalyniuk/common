from flask_restful import fields

house_structure = {
    "address": fields.String,
    "street_id": fields.Integer
}

street_structure = {
    "id": fields.Integer,
    "name": fields.String,
    "houses": fields.Nested(house_structure)
}
