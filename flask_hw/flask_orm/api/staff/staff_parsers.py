from flask_restful import reqparse


def positive_number(some_value, name):
    if name == 'room_number':
        try:
            some_value = int(some_value)
        except ValueError:
            msg = f"The parameter '{name}' must be int"
            raise ValueError(msg)
    if name == 'salary':
        try:
            some_value = float(some_value)
        except ValueError:
            msg = f"The parameter {name} must be float" \
                  f" Your value is: '{some_value}'"
            raise ValueError(msg)
    if some_value < 0:
        msg = f"The parameter '{name}' must be positive." \
              f" Your value is: {some_value}"
        raise ValueError(msg)
    return some_value


def data_valid_for(req):
    staff_args = ['passport_id', 'name', 'position', 'salary']
    valid_args = set(staff_args)
    parser = reqparse.RequestParser(bundle_errors=True)
    if req in ['POST', 'PUT', 'PATCH']:
        required = True
        if req == 'PATCH':
            required = False
        parser.add_argument('passport_id', required=required)
        parser.add_argument('name', required=required)
        parser.add_argument('position', required=required)
        parser.add_argument('salary', type=positive_number, required=required)
        data = parser.parse_args(strict=True)
        if all(data.values()) or req == 'PATCH':
            return {key: data[key] for key in data if data[key]}
        else:
            # can be used like (required=True and bundle_error=True) analog
            # todo: remove it
            not_none_keys = list(filter(lambda key: data[key], data))
            missing_args = list(valid_args ^ set(not_none_keys))
            return missing_args
    elif req == 'GET':
        parser.add_argument('name')
    return parser.parse_args(strict=True)


def data_valid_for_staff_room(req):

    parser = reqparse.RequestParser(bundle_errors=True)
    if req in ['POST', 'PUT', 'DELETE']:
        parser.add_argument('staff_name', required=True)
        parser.add_argument('room_number', type=positive_number, required=True)
        data = parser.parse_args(strict=True)
        return data
    elif req == 'GET':
        parser.add_argument('name')
    return parser.parse_args(strict=True)