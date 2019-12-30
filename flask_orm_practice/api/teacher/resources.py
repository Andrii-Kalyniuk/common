from flask_restful import Resource


class TeacherResource(Resource):
    def get(self):
        return "Ok"
