from flask_restful import reqparse


def positive_number(some_value, name):
    try:
        some_value = int(some_value)
    except ValueError:
        msg = f"The parameter '{name}' must be int"
        raise ValueError(msg)
    if some_value < 0:
        msg = f"The parameter '{name}' must be positive." \
              f" Your value is: {some_value}"
        raise ValueError(msg)
    return some_value


def data_valid_for(req):
    parser = reqparse.RequestParser(bundle_errors=True)
    if req in ['POST', 'PUT', 'PATCH']:
        required = True
        if req == 'PATCH':
            required = False
        parser.add_argument('name', required=required)
        parser.add_argument('passport_id', required=required)
        parser.add_argument('age', type=positive_number, required=required)
        parser.add_argument('sex', required=required)
        parser.add_argument('address', type=dict, required=required)
        parser.add_argument('room_number', type=positive_number,
                            required=required)
    elif req == 'GET':
        parser.add_argument('name')
        return parser.parse_args(strict=True)
    data = parser.parse_args(strict=True)
    return {key: data[key] for key in data if data[key]}
