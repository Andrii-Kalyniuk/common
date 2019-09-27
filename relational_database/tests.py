import json
import os
import unittest

import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from relational_database.config import TEST_DATABASE, DATABASE, FIXTURES_PATH
from relational_database.db_utils import init_tables, clear_tables, fill_tables, drop_tables
from relational_database.homework import \
    (task_1_add_new_record_to_db,
     task_2_list_all_customers,
     task_3_list_customers_in_germany,
     task_4_update_customer,
     task_5_delete_the_last_customer,
     task_6_list_all_supplier_countries,
     task_7_list_supplier_countries_in_desc_order,
     task_8_count_customers_by_city,
     task_9_count_customers_by_country_with_than_10_customers,
     task_10_list_first_10_customers,
     task_11_list_customers_starting_from_11th,
     task_12_list_suppliers_from_specified_countries,
     task_13_list_products_from_sweden_suppliers,
     task_14_list_products_with_supplier_information,
     task_15_list_customers_with_any_order_or_not,
     task_16_match_all_customers_and_suppliers_by_country
     )


class TestSQLQueries(unittest.TestCase):

    conn = None
    cur = None

    @staticmethod
    def drop_test_database_and_role(conn):
        with conn.cursor() as cursor:
            user = TEST_DATABASE.get('user')
            database = TEST_DATABASE.get('database')
            cursor.execute(f"DROP DATABASE IF EXISTS {database}")
            cursor.execute(f"SELECT 1 FROM pg_catalog.pg_user WHERE usename = '{user}'")
            if cursor.fetchone():
                cursor.execute(f"DROP ROLE {user}")
            conn.commit()


    @staticmethod
    def create_test_database_and_role(conn):
        with conn.cursor() as cursor:
            user = TEST_DATABASE.get('user')
            database = TEST_DATABASE.get('database')
            password = TEST_DATABASE.get('password')
            cursor.execute(f"CREATE ROLE {user} WITH LOGIN CREATEDB PASSWORD '{password}'")
            cursor.execute(f"CREATE DATABASE {database}")
            cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {database} to {user};")
            conn.commit()

    @classmethod
    def setUpClass(cls) -> None:
        root_conn = psycopg2.connect(**DATABASE)
        root_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cls.drop_test_database_and_role(root_conn)
        cls.create_test_database_and_role(root_conn)
        root_conn.close()

        conn = psycopg2.connect(**TEST_DATABASE)
        # with conn.cursor() as cursor:
        #     init_tables(cursor)
        conn.commit()
        conn.close()

    def setUp(self) -> None:
        self.conn = psycopg2.connect(**TEST_DATABASE)
        with self.conn.cursor() as cursor:
            init_tables(cursor)
            fill_tables(cursor)
        self.conn.commit()

    def tearDown(self) -> None:
        with self.conn.cursor() as cursor:
            clear_tables(cursor)
            drop_tables(cursor)
        self.conn.commit()
        self.conn.close()

    @classmethod
    def tearDownClass(cls) -> None:
        root_conn = psycopg2.connect(**DATABASE)
        root_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cls.drop_test_database_and_role(root_conn)
        root_conn.close()

    def test_task_1(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            task_1_add_new_record_to_db(self.conn)
            cursor.execute("SELECT * from customers;")
            actual_result = [dict(record) for record in cursor]
            expected_result = self.load_rows_from_file("task_1.json")
        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_2(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_2_list_all_customers(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_2.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_3(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_3_list_customers_in_germany(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_3.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_4(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            task_4_update_customer(self.conn)
            cursor.execute("SELECT * from customers;")
            actual_result = [dict(record) for record in cursor]
            expected_result = self.load_rows_from_file("task_4.json")
        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

        self.conn.commit()

    def test_task_5(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            task_5_delete_the_last_customer(self.conn)
            cursor.execute("SELECT * from customers;")
            actual_result = [dict(record) for record in cursor]
            expected_result = self.load_rows_from_file("task_5.json")
        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

        self.conn.commit()

    def test_task_6(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_6_list_all_supplier_countries(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_6.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_7(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_7_list_supplier_countries_in_desc_order(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_7.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_8(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_8_count_customers_by_city(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_8.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_9(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_9_count_customers_by_country_with_than_10_customers(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_9.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_10(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_10_list_first_10_customers(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_10.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_11(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_11_list_customers_starting_from_11th(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_11.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_12(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_12_list_suppliers_from_specified_countries(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_12.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_13(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_13_list_products_from_sweden_suppliers(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_13.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_14(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_14_list_products_with_supplier_information(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_14.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_15(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_15_list_customers_with_any_order_or_not(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_15.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def test_task_16(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            actual_result = task_16_match_all_customers_and_suppliers_by_country(cursor)
            actual_result = [dict(record) for record in actual_result]
            expected_result = self.load_rows_from_file("task_16.json")

        for i, row in enumerate(actual_result):
            self.assertDictEqual(row, expected_result[i])

    def load_rows_from_file(self, file_name):
        file = os.path.join(FIXTURES_PATH, "tests_results", file_name)
        with open(file) as json_file:
            data = json.load(json_file)
        return data


if __name__ == "__main__":
    unittest.main()
