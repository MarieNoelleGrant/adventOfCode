import unittest
# from day07_outputSignal import find_max_thruster_signal
from modules.intcode_computer import test_program
import math


# ===============================================================================================
#   DAY 07
# ===============================================================================================

class TestsMaxThrusterSignal(unittest.TestCase):

    def test_expected_value(self):
        pass
        # self.assertEqual(find_max_thruster_signal(
        #     [3, 15, 3, 6, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
        #     [['4', '3', '2', '1', '0']]), 43210)
        # self.assertEqual(find_max_thruster_signal(
        #     [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
        #     [['0', '1', '2', '3', '4']]), 54321)
        # self.assertEqual(find_max_thruster_signal(
        #     [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32,
        #      31, 31, 4, 31, 99, 0, 0, 0], [['1', '0', '4', '3', '2']]), 65210)
        # self.assertEqual(find_max_thruster_signal(
        #     [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99,
        #      0, 0, 5], [['9', '8', '7', '6', '5']]), 139629729)
        # self.assertEqual(find_max_thruster_signal(
        #     [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1,
        #      12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6,
        #      99, 0, 0, 0, 0, 10], [['9', '7', '8', '5', '6']]), 18216)


class TestBoostProgramOptions(unittest.TestCase):

    def test_new_options_intcode(self):
        # Test pour vérifier si le programme se renvoie lui même (ajuster la valeur retournée du optcode 4!)
        # self.assertEqual(test_program([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]), '01091204-1100110011001008100161011006101099')

        # Test pour vérifier la longeur du résultat reçu (devrait contenir 16 digits)
        # self.assertEqual(round(math.log10(test_program([1102, 34915192, 34915192, 7, 4, 7, 99, 0])) + 1), 16)

        self.assertEqual(test_program([104, 1125899906842624, 99]), 1125899906842624)


if __name__ == '__main__':
    unittest.main()
