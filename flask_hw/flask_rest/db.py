import logging


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

staff_rooms = db.Table(
    'staff_rooms',
    db.Column('room_number', db.Integer, db.ForeignKey('rooms.number')),
    db.Column('staff_id', db.String, db.ForeignKey('staff.passport_id'))
)


class Rooms(db.Model):
    number = db.Column(db.Integer, unique=True, primary_key=True)
    level = db.Column(db.String(80))
    status = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    tenant_id = db.Column(db.String, db.ForeignKey('tenants.passport_id'))


class Staff(db.Model):
    passport_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    rooms = db.relationship('Rooms', secondary=staff_rooms, backref='serve_by')


class Tenants(db.Model):
    passport_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(5))
    city = db.Column(db.String(80))
    address = db.Column(db.String(80))
    rooms = db.relation('Rooms', backref='rooms')


def fill_up_db():
    db.session.remove()
    db.drop_all()
    db.session.commit()
    logging.info('---Previous database has been DELETED---')
    db.create_all()
    room_0 = Rooms(number=42, level='Lux', status='closed', price=1000,
                   tenant_id='cc3333')
    room_1 = Rooms(number=7, level='Classic', status='available',
                   price=59.99, tenant_id='cc3333')
    room_2 = Rooms(number=69, level='VIP', status='available',
                   price=9000, tenant_id='zz0101')
    room_3 = Rooms(number=11, level='Loft', status='closed', price=10,
                   tenant_id='zz0101')
    staff_0 = Staff(passport_id='aa1111', name='Taylor',
                    position='waiter', salary=100.0)
    staff_1 = Staff(passport_id='et0000', name='Hannibal',
                    position='cook', salary=1000)
    staff_2 = Staff(passport_id='ad1234', name='Hilton',
                    position='Administrator', salary=9000)

    tenant_0 = Tenants(passport_id='zz0101', name='Neo', age=33,
                       sex='M', city='Zeon', address='Street 255')
    tenant_1 = Tenants(passport_id='bb2222', name='Janis', age=40,
                       sex='W', city='Los Angeles',
                       address='Beverly Hills, 90210')
    tenant_2 = Tenants(passport_id='cc3333', name='Sherlock', age=51,
                       sex='M', city='London',
                       address='Bakerstreet, 221B')
    db.session.add(room_0)
    db.session.add(room_1)
    db.session.add(room_2)
    db.session.add(room_3)
    db.session.add(staff_0)
    db.session.add(staff_1)
    db.session.add(staff_2)
    db.session.add(tenant_0)
    db.session.add(tenant_1)
    db.session.add(tenant_2)
    logging.info('---The database was FILLED with test values---')
    db.session.commit()
