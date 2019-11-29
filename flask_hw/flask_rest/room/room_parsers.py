from flask_restful import reqparse


def positive_number(some_value, name):
    if name in ('number', 'level'):
        try:
            some_value = int(some_value)
        except ValueError:
            msg = f"The parameter '{name}' must be int"
            raise ValueError(msg)
    if name == 'price':
        try:
            some_value = float(some_value)
        except ValueError:
            msg = f"The parameter {name} must be float"
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
        parser.add_argument('number', type=positive_number, required=required)
        parser.add_argument('level', type=positive_number, required=required)
        parser.add_argument('status', required=required)
        parser.add_argument('price', type=positive_number, required=required)
    elif req == 'GET':
        parser.add_argument('status')
        return parser.parse_args(strict=True)
    data = parser.parse_args(strict=True)
    return {key: data[key] for key in data if data[key]}
