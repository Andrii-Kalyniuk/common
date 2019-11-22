from flask_restful import reqparse


def data_valid_for(req):
    valid_args = set(['number', 'level', 'status', 'price'])
    parser = reqparse.RequestParser()
    if req in ['POST', 'PUT']:
        parser.add_argument('number', type=int)
        parser.add_argument('level')
        parser.add_argument('status')
        parser.add_argument('price', type=float)
        data = parser.parse_args(strict=True)
        if all(data.values()):
            return data
        else:
            not_none_keys = list(filter(lambda key: data[key], data))
            missing_args = list(valid_args ^ set(not_none_keys))
            return missing_args
    elif req == 'GET':
        parser.add_argument('status')
    return parser.parse_args(strict=True)

