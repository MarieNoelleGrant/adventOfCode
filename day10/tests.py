import unittest
from monitoringStation import initialisation


# ===============================================================================================
#   DAY 10
# ===============================================================================================

class TestsAsteroidSighting(unittest.TestCase):

    def test_expected_value(self):
        # ** must change input_day10.txt for each test
        # self.assertEqual(initialisation(), 33)
        # self.assertEqual(initialisation(), 35)
        # self.assertEqual(initialisation(), 41)
        self.assertEqual(initialisation(), 210)


if __name__ == '__main__':
    unittest.main()
