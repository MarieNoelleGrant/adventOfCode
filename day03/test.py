# from fuelCounter import calc_fuel_needed
import unittest
# *** Je ne sais pas pourquoi il ne reconnaît pas mon module, mais ça fonctionne quand même.
from wireControl_part1 import calcul_manhattan_distance, create_coordinates, creation_intersections
# import computerEmulation


class TestDistanceManhattan(unittest.TestCase):

    def test_calc_point_plus_proche(self):
        self.assertEqual(calcul_manhattan_distance(creation_intersections(create_coordinates(['R75','D30','R83','U83','L12','D49','R71','U7','L72']), create_coordinates(['U62','R66','U55','R34','D71','R55','D58','R83']))), 159)
        self.assertEqual(calcul_manhattan_distance(creation_intersections(create_coordinates(['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']), create_coordinates(['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']))), 135)


if __name__ == '__main__':
    unittest.main()
