from flask_restful import fields

news_structure = {
    "id": fields.Integer,
    "title": fields.String,
    "text": fields.String,
    "date": fields.DateTime
}
