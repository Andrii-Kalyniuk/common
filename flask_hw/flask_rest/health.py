from flask_restful import Resource


class HealthCheck(Resource):
    def get(self):
        return {'server_health': 'OK'}
