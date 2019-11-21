from flask_restful import Resource, request


class SchoolResource(Resource):
    def get(self):
        return "Ok"
