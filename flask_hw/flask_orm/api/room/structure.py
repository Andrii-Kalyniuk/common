from flask_restful import fields

room_structure = {
    "number": fields.Integer,
    "level": fields.String,
    "status": fields.String,
    "price": fields.Float,
    "tenant_id": fields.String
}
