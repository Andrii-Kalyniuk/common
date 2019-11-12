from models import Room, Staff, Tenants

DB = {}

def fillup_db():
    DB['rooms'].append(Room(42, 'Lux', 'closed', 1000))
    DB['rooms'].append(Room(7, 'Classic', 'available', 50))
    DB['rooms'].append(Room(69, 'VIP', 'available', 9000))
    DB['rooms'].append(Room(11, 'Loft', 'closed', 10))

    DB['tenants'].append(Tenants('Neo', 33, 'M', 'Street 255', 42))
    DB['tenants'].append(Tenants('Janis', 40, 'W', 'Street 255', 7))
    DB['tenants'].append(Tenants('Sherlock', 51, 'M', 'Bakerstreet, 221B', 11))

    DB['staff'].append(Staff('Taylor', 'waiter', 100))
    DB['staff'].append(Staff('Hannibal', 'cook', 1000))
    DB['staff'].append(Staff('Hilton', 'Administrator', 9000))
