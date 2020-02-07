# from fuelCounter import calc_fuel_needed
import unittest
# *** Je ne sais pas pourquoi il ne reconnaît pas mon module, mais ça fonctionne quand même.
import fuelCounter


class TestFuelCalc(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(fuelCounter.calc_fuel_needed(12), 2)
        self.assertEqual(fuelCounter.calc_fuel_needed(14), 2)
        self.assertEqual(fuelCounter.calc_fuel_needed(1969), 654)
        self.assertEqual(fuelCounter.calc_fuel_needed(100756), 33583)


if __name__ == '__main__':
    unittest.main()
