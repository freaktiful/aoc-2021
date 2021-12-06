import unittest
import numpy

from main import format_input, part_1, part_2


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):
        """
        Test the correct formatting of the input data
        """
        formatted_input = format_input('test_input.txt')
        self.assertEquals(part_1(formatted_input), 5934)
        self.assertEquals(part_2(formatted_input), 26984457539)


if __name__ == '__main__':
    unittest.main()