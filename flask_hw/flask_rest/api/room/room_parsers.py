from flask_restful import reqparse


def data_valid_for(req):
    parser = reqparse.RequestParser(bundle_errors=True)
    if req in ['POST', 'PUT']:
        parser.add_argument('number', type=int, required=True)
        parser.add_argument('level', required=True)
        parser.add_argument('status', required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('tenant_id')
        data = parser.parse_args(strict=True)
        return data
    elif req == 'GET':
        parser.add_argument('status')
    return parser.parse_args(strict=True)

