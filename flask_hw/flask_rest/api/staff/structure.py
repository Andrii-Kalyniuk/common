from flask_restful import fields

serviced_rooms = {
    "number": fields.Integer,
    "level": fields.String
}

staff_structure = {
    "passport_id": fields.String,
    "name": fields.String,
    "position": fields.String,
    "salary": fields.Float,
    "rooms": fields.Nested(serviced_rooms)
}
