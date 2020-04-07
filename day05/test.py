import unittest
import TEST_program


class TestMotPassePossible(unittest.TestCase):

    def test_optcodes_part2(self):
        # Tests optcode 8 ---------------------------------------------------------------------
        print(f'*** Donner le chiffre 8 lorsque demandé --------------------------------------------')
        self.assertEqual(TEST_program.test_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]), 1)
        self.assertEqual(TEST_program.test_program([3, 3, 1108, -1, 8, 3, 4, 3, 99]), 1)
        print(f'*** Donner tout autre chiffre que 8 lorsque demandé --------------------------------------------')
        self.assertEqual(TEST_program.test_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]), 0)
        self.assertEqual(TEST_program.test_program([3, 3, 1108, -1, 8, 3, 4, 3, 99]), 0)

        # Tests optcode 7 ---------------------------------------------------------------------
        print(f'*** Donner un chiffre plus petit que 8 lorsque demandé --------------------------------------------')
        self.assertEqual(TEST_program.test_program([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]), 1)
        self.assertEqual(TEST_program.test_program([3, 3, 1107, -1, 8, 3, 4, 3, 99]), 1)
        print(f'*** Donner un chiffre plus grand ou égal à 8 lorsque demandé --------------------------------------------')
        self.assertEqual(TEST_program.test_program([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]), 0)
        self.assertEqual(TEST_program.test_program([3, 3, 1107, -1, 8, 3, 4, 3, 99]), 0)

        # Tests optcode 5 et 6 ---------------------------------------------------------------------
        print(f'*** Donner le chiffre 0 lorsque demandé --------------------------------------------')
        self.assertEqual(TEST_program.test_program([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]), 0)
        self.assertEqual(TEST_program.test_program([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]), 0)
        print(f'*** Donner tout autre chiffre que 0 lorsque demandé --------------------------------------------')
        self.assertEqual(TEST_program.test_program([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]), 1)
        self.assertEqual(TEST_program.test_program([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]), 1)

        # Test global
        print('*** Donner un chiffre plus petit que 8')
        self.assertEqual(TEST_program.test_program([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]), 999)
        print('*** Donner le chiffre 8')
        self.assertEqual(TEST_program.test_program([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]), 1000)
        print('*** Donner un chiffre plus grand que 8')
        self.assertEqual(TEST_program.test_program([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]), 1001)


if __name__ == '__main__':
    unittest.main()
