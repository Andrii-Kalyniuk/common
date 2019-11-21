from flask_restful import Resource, request


class DiaryResource(Resource):
    def get(self):
        return "Ok"
