from models import Room, Staff, Tenant

DB = {}


def fillup_db():
    DB['rooms'].append(Room(42, 'Lux', 'closed', 1000))
    DB['rooms'].append(Room(7, 'Classic', 'available', 50))
    DB['rooms'].append(Room(69, 'VIP', 'available', 9000))
    DB['rooms'].append(Room(11, 'Loft', 'closed', 10))

    DB['tenants'].append(Tenant('Neo', 33, 'M',
                                {
                                    "city": "Zeon",
                                    "street": "Street 255"
                                }, 42))
    DB['tenants'].append(Tenant('Janis', 40, 'W',
                                {
                                    "city": "Los Angeles",
                                    "street": "Beverly Hills, 90210"
                                }, 7))
    DB['tenants'].append(Tenant('Sherlock', 51, 'M',
                                {
                                    "city": "London",
                                    "street": "Bakerstreet, 221B"
                                }, 11))

    DB['staff'].append(Staff('Taylor', 'waiter', 100))
    DB['staff'].append(Staff('Hannibal', 'cook', 1000))
    DB['staff'].append(Staff('Hilton', 'Administrator', 9000))
