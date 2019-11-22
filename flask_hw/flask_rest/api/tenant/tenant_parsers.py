from flask_restful import reqparse


def data_valid_for(req):
    tenant_args = ['passport_id', 'name', 'age', 'sex', 'city', 'address']
    valid_args = set(tenant_args)
    parser = reqparse.RequestParser()
    if req in ['POST', 'PUT']:
        parser.add_argument('passport_id')
        parser.add_argument('name')
        parser.add_argument('age', type=int)
        parser.add_argument('sex')
        parser.add_argument('city')
        parser.add_argument('address')
        data = parser.parse_args(strict=True)
        if all(data.values()):
            return data
        else:
            not_none_keys = list(filter(lambda key: data[key], data))
            missing_args = list(valid_args ^ set(not_none_keys))
            return missing_args
    elif req == 'GET':
        parser.add_argument('name')
    return parser.parse_args(strict=True)

