import json

from flask import request
from flask_restful import Resource, marshal_with

from db import db

from many_to_many_example.parser import author_book_parser

from many_to_many_example.structures import book_structure, author_structure
from models.many_to_many_example import Book, Author


class BookView(Resource):
    @marshal_with(book_structure)
    def get(self):
        return Book.query.all()

    def post(self):
        data = json.loads(request.data)
        book = Book(**data)
        db.session.add(book)
        db.session.commit()
        return "Successfully added"


class AuthorView(Resource):
    @marshal_with(author_structure)
    def get(self):
        return Author.query.all()

    def post(self):
        data = json.loads(request.data)
        author = Author(**data)
        db.session.add(author)
        db.session.commit()
        return "Successfully added"


class AuthorBook(Resource):
    def post(self):
        data = json.loads(request.data)
        author_name = data.get("author_name")
        book_name = data.get("book_name")
        author = Author.query.filter_by(name=author_name).first()
        book = Book.query.filter_by(name=book_name).first()
        author.works.append(book)
        db.session.commit()
        return f"Successfully added {book.name} to {author.name}"

    @marshal_with(book_structure)
    def get(self):
        args = author_book_parser.parse_args(strict=True)
        author = Author.query.filter_by(name=args.get("name")).first()
        return author.works
