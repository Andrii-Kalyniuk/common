from flask_restful import reqparse


def positive_number(some_value, name):
    try:
        some_value = int(some_value)
    except ValueError:
        msg = f"The parameter '{name}' must be int" \
              f" Your value is: '{some_value}'"
        raise ValueError(msg)
    if some_value < 0:
        msg = f"The parameter '{name}' must be positive." \
              f" Your value is: {some_value}"
        raise ValueError(msg)
    return some_value


def data_valid_for(req):
    tenant_args = ['passport_id', 'name', 'age', 'sex', 'city', 'address']
    valid_args = set(tenant_args)
    parser = reqparse.RequestParser()
    if req in ['POST', 'PUT', 'PATCH']:
        parser.add_argument('passport_id')
        parser.add_argument('name')
        parser.add_argument('age', type=positive_number)
        parser.add_argument('sex')
        parser.add_argument('city')
        parser.add_argument('address')
        data = parser.parse_args(strict=True)
        if all(data.values()) or req == 'PATCH':
            return {key: data[key] for key in data if data[key]}
        # working like (required=True and bundle_error=True) analog
        else:
            not_none_keys = list(filter(lambda key: data[key], data))
            missing_args = list(valid_args ^ set(not_none_keys))
            return missing_args
    elif req == 'GET':
        parser.add_argument('name')
    return parser.parse_args(strict=True)
