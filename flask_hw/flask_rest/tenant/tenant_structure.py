from flask_restful import fields

address_structure = {
    "city": fields.String,
    "street": fields.String
}
tenant_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "address": fields.Nested(address_structure),
    "room_number": fields.Integer
}
