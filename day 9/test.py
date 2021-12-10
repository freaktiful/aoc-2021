import unittest
import numpy

from main import format_input, find_low_points, find_basins


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):
        """
        Test the correct formatting of the input data
        """
        formatted_input = format_input('test_input.txt')
        numpy.testing.assert_array_equal(formatted_input, [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                                                           [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                                                           [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                                                           [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                                                           [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])
        self.assertEquals(find_low_points(formatted_input), 15)
        self.assertEquals(find_basins(formatted_input), 1134)


if __name__ == '__main__':
    unittest.main()