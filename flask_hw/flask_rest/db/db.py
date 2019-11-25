from models import Room, Staff, Tenant

DB = {}


def fillup_db():
    DB['rooms'].append(Room(42, 'Lux', 'closed', 1000))
    DB['rooms'].append(Room(7, 'Classic', 'available', 50))
    DB['rooms'].append(Room(69, 'VIP', 'available', 9000))
    DB['rooms'].append(Room(11, 'Loft', 'closed', 10))

    DB['tenants'].append(Tenant('Neo', 'zz0101', 33, 'M',
                                {
                                    "city": "Zeon",
                                    "street": "Street 255"
                                }, 42))
    DB['tenants'].append(Tenant('Janis', 'bb2222', 40, 'W',
                                {
                                    "city": "Los Angeles",
                                    "street": "Beverly Hills, 90210"
                                }, 7))
    DB['tenants'].append(Tenant('Sherlock', 'cc3333', 51, 'M',
                                {
                                    "city": "London",
                                    "street": "Bakerstreet, 221B"
                                }, 11))

    DB['staff'].append(Staff('Taylor', 'aa1111', 'waiter', 100))
    DB['staff'].append(Staff('Hannibal', 'et0000', 'cook', 1000))
    DB['staff'].append(Staff('Hilton', 'ad1234', 'Administrator', 9000))
