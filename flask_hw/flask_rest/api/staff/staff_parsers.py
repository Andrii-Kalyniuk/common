from flask_restful import reqparse


def data_valid_for(req):
    staff_args = ['passport_id', 'name', 'position', 'salary']
    valid_args = set(staff_args)
    parser = reqparse.RequestParser(bundle_errors=True)
    if req in ['POST', 'PUT']:
        parser.add_argument('passport_id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('position', required=True)
        parser.add_argument('salary', type=float, required=True)
        data = parser.parse_args(strict=True)
        if all(data.values()):
            return data
        else:
            # can be used like "required=True" analog
            not_none_keys = list(filter(lambda key: data[key], data))
            missing_args = list(valid_args ^ set(not_none_keys))
            return missing_args
    elif req == 'GET':
        parser.add_argument('name')
    return parser.parse_args(strict=True)

