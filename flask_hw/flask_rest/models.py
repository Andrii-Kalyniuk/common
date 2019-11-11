import uuid


class Room:

    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price
        self.id = str(uuid.uuid4())


class Tenants:

    def __init__(self, name, passport_id, age,
                 sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.sex = address
        self.sex = room_number


class Staff:

    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary
