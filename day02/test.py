# from fuelCounter import calc_fuel_needed
import unittest
# *** Je ne sais pas pourquoi il ne reconnaît pas mon module, mais ça fonctionne quand même.
from program_part1 import rebuilt_intcode_program
# import computerEmulation

class TestComputerRebuilding(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(rebuilt_intcode_program([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
        self.assertEqual(rebuilt_intcode_program([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
        self.assertEqual(rebuilt_intcode_program([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(rebuilt_intcode_program([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == '__main__':
    unittest.main()
