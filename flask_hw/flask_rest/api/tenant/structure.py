from flask_restful import fields

tenant_structure = {
    "passport_id": fields.String,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "city": fields.String,
    "address": fields.String
}