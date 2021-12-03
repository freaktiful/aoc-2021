import unittest
import numpy

from main import format_input, part_1, part_2


class TestSum(unittest.TestCase):
    def test_day_3(self):
        """
        Test that it sums the columns of the matrix
        """
        array_data = format_input('test_input.txt')
        self.assertEqual(part_1(array_data), 198)
        self.assertEqual(part_2(array_data, 0, True), 23)
        self.assertEqual(part_2(array_data, 0, False), 10)


if __name__ == '__main__':
    unittest.main()