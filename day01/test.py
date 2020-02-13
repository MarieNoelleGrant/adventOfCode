import unittest

import fuelCounter
import fuelCounter_part2


class TestFuelCalc(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(fuelCounter.calc_fuel_needed(12), 2)
        self.assertEqual(fuelCounter.calc_fuel_needed(14), 2)
        self.assertEqual(fuelCounter.calc_fuel_needed(1969), 654)
        self.assertEqual(fuelCounter.calc_fuel_needed(100756), 33583)

    def test_calc_part2(self):
        self.assertEqual(fuelCounter_part2.calc_fuel_needed(14), 2)
        self.assertEqual(fuelCounter_part2.calc_fuel_needed(1969), 966)
        self.assertEqual(fuelCounter_part2.calc_fuel_needed(100756), 50346)

if __name__ == '__main__':
    unittest.main()
