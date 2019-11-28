from flask import Flask
from flask_restful import Api

from config import get_config
from db.db import DB, fillup_db
from room import rooms_bp
from staff import staff_bp
from tenant import tenants_bp
from health import HealthCheck


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

api = Api(app, catch_all_404s=True)
api.add_resource(HealthCheck, '/_health_check')

if __name__ == "__main__":
    app.config.from_object(get_config())
    app.run()
