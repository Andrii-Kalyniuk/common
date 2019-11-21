from flask import Blueprint
from flask_restful import Api
from auth.routes import Login, Logout, Registration

auth = Blueprint("auth", __name__)
api = Api(auth)

api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(Registration, "/auth")
