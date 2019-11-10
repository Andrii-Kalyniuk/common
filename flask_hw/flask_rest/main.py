from flask import Flask
from flask_restful import Api

from config import run_config
from db.db import DB
from routes.health import HealthCheck
from routes.rooms import Rooms


def db_setup():
    DB['rooms'] = []
    DB['tenants'] = []
    DB['staff'] = []


db_setup()
app = Flask(__name__)
api = Api(app)
api.add_resource(HealthCheck, '/_health_check')
api.add_resource(Rooms, '/rooms')

if __name__ == "__main__":
    app.config.from_object(run_config())
    app.run()
