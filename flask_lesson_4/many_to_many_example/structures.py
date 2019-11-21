from flask_restful import fields

book_structure = {
    "name": fields.String
}

author_structure = {
    "name": fields.String,
    "works": fields.Nested(book_structure)
}
