import unittest
import numpy

from main import format_input, fold_paper, fold_all, print_result


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):

        initial_paper, folding_orders = format_input('test_input.txt')
        self.assertEqual(len(fold_paper(initial_paper, folding_orders[0])), 17)


if __name__ == '__main__':
    unittest.main()