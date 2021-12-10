import unittest

from main import format_input, count_unique_digits_in_output, solve_display


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):
        """
        Test the correct formatting of the input data
        """
        formatted_input = format_input('test_input.txt')
        self.assertEquals(count_unique_digits_in_output(formatted_input), 26)
        self.assertEquals(solve_display(formatted_input), 61229)


if __name__ == '__main__':
    unittest.main()