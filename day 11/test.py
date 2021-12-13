import unittest
import numpy as np

from main import format_input, make_fixed_number_of_flashes, min_number_steps_for_all_flashes


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):
        """
        Test the correct formatting of the input data
        """
        formatted_input = np.array(format_input('test_input.txt'))
        self.assertEquals(make_fixed_number_of_flashes(formatted_input), 1656)
        self.assertEquals(min_number_steps_for_all_flashes(formatted_input), 195)


if __name__ == '__main__':
    unittest.main()
