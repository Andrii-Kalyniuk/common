import json


def get_data():
    with open("data.json") as file:
        return json.load(file)
