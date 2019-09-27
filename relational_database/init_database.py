import psycopg2

from relational_database.config import DATABASE
from relational_database.db_utils import init_tables, fill_tables

if __name__ == "__main__":
    con = psycopg2.connect(**DATABASE)
    with con.cursor() as cursor:
        try:
            init_tables(cursor)
            fill_tables(cursor)
            con.commit()
        finally:
            if con:
                con.close()
