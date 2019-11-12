from flask import Flask
from flask_restful import Api

from config import run_config
from db.db import DB
from models import Room
from routes.health import HealthCheck
from routes.rooms import Rooms


def db_setup():
    DB['rooms'] = []
    DB['tenants'] = []
    DB['staff'] = []

    DB['rooms'].append(Room(42, 'vip', 'closed', 1000.50))
    DB['rooms'].append(Room(7, 'vip', 'available', 9000))
    DB['rooms'].append(Room(69, 'vip', 'available', 150))



db_setup()
app = Flask(__name__)
api = Api(app)
api.add_resource(HealthCheck, '/_health_check')
api.add_resource(Rooms, '/api/v0.1/rooms', '/api/v0.1/rooms/<id_>')

if __name__ == "__main__":
    app.config.from_object(run_config())
    app.run()
