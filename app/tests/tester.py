import unittest
from flask import current_app


class TestUM(unittest.TestCase):

    def setUp(self):
        database = current_app._get_current_object().database
        database.addMatch("21")
        print(1)

    def test_False(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
