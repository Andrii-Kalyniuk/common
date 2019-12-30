from flask_restful import Resource


class StudentResource(Resource):
    def get(self):
        return "Ok"
