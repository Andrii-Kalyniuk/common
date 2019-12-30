import json

DB = {}

with open('db/test_db.json') as db_file:
    DB_test = json.load(db_file)
