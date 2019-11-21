from flask_restful import Resource


class StudiosResource(Resource):
    def get(self):
        return "studios"
