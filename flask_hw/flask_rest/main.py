from flask import Flask
from flask_restful import Api

from config import run_config
from db.db import DB, fillup_db
from api.room import rooms_bp
from api.staff import staff_bp
from api.tenant import tenants_bp
from api.health import HealthCheck


def db_setup():
    DB['rooms'] = []
    DB['tenants'] = []
    DB['staff'] = []
    fillup_db()


db_setup()
app = Flask(__name__)
app.register_blueprint(rooms_bp)
app.register_blueprint(tenants_bp)
app.register_blueprint(staff_bp)

api = Api(app)
api.add_resource(HealthCheck, '/_health_check')

if __name__ == "__main__":
    app.config.from_object(run_config())
    app.run()
