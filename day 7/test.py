import unittest

from main import format_input, greedy, median


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):
        """
        Test the correct formatting of the input data
        """
        formatted_input = format_input('test_input.txt')
        self.assertEquals(greedy(formatted_input, False), (2, 37))
        self.assertEquals(median(formatted_input), (2, 37))
        self.assertEquals(greedy(formatted_input, True), (5, 168))


if __name__ == '__main__':
    unittest.main()