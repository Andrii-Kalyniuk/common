import uuid


class Room:

    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price
        self.id = str(uuid.uuid4())

    def serialize(self):
        return self.__dict__


class Tenant:

    def __init__(self, name, age, sex, address, room_number):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number
        self.passport_id = str(uuid.uuid4())


class Staff:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.passport_id = str(uuid.uuid4())
