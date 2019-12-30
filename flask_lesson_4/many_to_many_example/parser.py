from flask_restful import reqparse

author_book_parser = reqparse.RequestParser()
author_book_parser.add_argument("name", required=True, help="Important: {error_msg}!!!")
