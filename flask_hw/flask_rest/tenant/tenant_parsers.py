from flask_restful import reqparse


def data_valid_for(req):
    parser = reqparse.RequestParser(bundle_errors=True)
    if req in ['POST', 'PUT']:
        parser.add_argument('name', required=True)
        parser.add_argument('passport_id', required=True)
        parser.add_argument('age', type=int, required=True)
        parser.add_argument('sex', required=True)
        parser.add_argument('address', type=dict, required=True)
        parser.add_argument('room_number', type=int, required=True)
    elif req == 'GET':
        parser.add_argument('name')
    return parser.parse_args(strict=True)
