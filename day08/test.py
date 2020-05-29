import unittest
from bios_password import decode_image


# ===============================================================================================
#   DAY 07
# ===============================================================================================

class TestsImageDecoding(unittest.TestCase):

    def test_expected_value(self):
        self.assertEqual(decode_image(), '0110')


if __name__ == '__main__':
    unittest.main()
