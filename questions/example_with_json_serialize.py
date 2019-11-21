import json
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Restaurant):
            return o.__dict__
        if isinstance(o, City):
            return {"name_of_city": o.name}
        raise TypeError


class Restaurant:
    def __init__(self, name):
        self.name = name


class City:
    def __init__(self, name):
        self.name = name

city = City("Lviv")
restaurant = Restaurant("YaponaHata")
# print(json.dumps(restaurant))
print(json.dumps(restaurant, cls=MyEncoder))
print(json.dumps(city, cls=MyEncoder))


