from flask_restful import reqparse

auth_parser = reqparse.RequestParser()
auth_parser.add_argument('login', required=True)
auth_parser.add_argument('password', required=True)
