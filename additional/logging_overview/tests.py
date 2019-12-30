import unittest
from unittest import mock

import testfixtures

from main import pay_developer


class TestDevelopersSalary(unittest.TestCase):

    @mock.patch('builtins.input', lambda *args: 'y')
    def test_normal_salary(self):
        with testfixtures.LogCapture() as logs:
            pay_developer(180)

        first_record = logs.records[0]
        self.assertEqual(first_record.msg, f"We get 180 hours of work")
        self.assertEqual(first_record.levelname, "DEBUG")


if __name__ == "__main__":
    unittest.main()
