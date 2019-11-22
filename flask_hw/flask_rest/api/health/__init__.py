from flask import Blueprint
from flask_restful import Api

from api.health.health import HealthCheck

health_bp = Blueprint('health', __name__)
health_api = Api(health_bp)
health_api.add_resource(HealthCheck, '/_health_check')

