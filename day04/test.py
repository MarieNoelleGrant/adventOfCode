import unittest
import passwordFinder_part1, passwordFinder_part2


class TestMotPassePossible(unittest.TestCase):

    def test_mdp_possible(self):
        self.assertIn(111111, passwordFinder_part1.calculate_possibilities(100000, 120000))
        self.assertNotIn(223450, passwordFinder_part1.calculate_possibilities(223300, 223600))
        self.assertNotIn(123789, passwordFinder_part1.calculate_possibilities(100000, 130000))

    def test_mdp_possible_plus(self):
        self.assertIn(112233, passwordFinder_part2.calculate_possibilities(112230, 112234))
        self.assertNotIn(123444, passwordFinder_part2.calculate_possibilities(123442, 123445))
        self.assertIn(111122, passwordFinder_part2.calculate_possibilities(111120, 111124))
        self.assertIn(255666, passwordFinder_part2.calculate_possibilities(255664, 255667))
        self.assertNotIn(333444, passwordFinder_part2.calculate_possibilities(333442, 333446))


if __name__ == '__main__':
    unittest.main()
