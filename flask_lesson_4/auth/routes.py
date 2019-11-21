from flask_restful import Resource
from flask import session
from auth.parsers import auth_parser

user = dict()


class Login(Resource):
    def post(self):
        """
        Add to session new value logged_in = True and return success msg
        if news registered and put correct login and password
        :return: str
        """
        args = auth_parser.parse_args(strict=True)
        name = args.get("login")
        password = args.get("password")
        if not user:
            return "There is no users in our system, please register", 401

        if name == user.get("login") and password == user.get("password"):
            session["logged_in"] = True
            return "You are successfully logged in"
        else:
            return "Wrong login or password", 403


class Logout(Resource):
    def get(self):
        """
        Change logged_in session value to False, which means that our decorator
        won't give access to see the page content from views where is it set.
        :return: str
        """
        session["logged_in"] = False
        return "You are successfully logged out"


class Registration(Resource):
    def post(self):
        """
        Add new news to dict news if he put all arguments
        :return:
        """
        args = auth_parser.parse_args(strict=True)
        user["login"] = args.get("login")
        user["password"] = args.get("password")
        return "Successfully registered"
