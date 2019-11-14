from flask import Flask
from flask_restful import Api

from config import run_config
from db.db import DB, fillup_db
from routes.health import HealthCheck
from routes.rooms import Rooms
from routes.staff import StaffRes
from routes.tenants import Tenants


def db_setup():
    DB['rooms'] = []
    DB['tenants'] = []
    DB['staff'] = []
    fillup_db()


db_setup()
app = Flask(__name__)
api = Api(app)
api.add_resource(HealthCheck, '/_health_check')
api.add_resource(Rooms, '/api/v0.1/rooms', '/api/v0.1/rooms/<id_>')
api.add_resource(StaffRes, '/api/v0.1/staff', '/api/v0.1/staff/<id_>')
api.add_resource(Tenants, '/api/v0.1/tenants', '/api/v0.1/tenants/<id_>')

if __name__ == "__main__":
    app.config.from_object(run_config())
    app.run()
