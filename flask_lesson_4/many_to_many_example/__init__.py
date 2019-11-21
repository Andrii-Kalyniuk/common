from flask import Blueprint
from flask_restful import Api

from many_to_many_example.routes import AuthorView, BookView, AuthorBook

many_to_many = Blueprint("many_to_many", __name__)
api_many_to_many = Api(many_to_many)

api_many_to_many.add_resource(AuthorView, "/author")
api_many_to_many.add_resource(BookView, "/book")
api_many_to_many.add_resource(AuthorBook, "/author_book")
