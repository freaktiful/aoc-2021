import unittest

from main import format_input, Graph


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):

        formatted_input = format_input('test_input.txt')
        g = Graph(formatted_input, 1)
        g.find_all_paths('start', 'end')

        g2 = Graph(formatted_input, 2)
        g2.find_all_paths('start', 'end')
        self.assertEqual(g.return_number_of_paths(), 10)
        self.assertEqual(g2.return_number_of_paths(), 36)

        formatted_input = format_input('test_input_2.txt')
        g = Graph(formatted_input, 1)
        g.find_all_paths('start', 'end')

        g2 = Graph(formatted_input, 2)
        g2.find_all_paths('start', 'end')
        self.assertEqual(g.return_number_of_paths(), 19)
        self.assertEqual(g2.return_number_of_paths(), 103)

        formatted_input = format_input('test_input_3.txt')
        g = Graph(formatted_input, 1)
        g.find_all_paths('start', 'end')

        g2 = Graph(formatted_input, 2)
        g2.find_all_paths('start', 'end')
        self.assertEqual(g.return_number_of_paths(), 226)
        self.assertEqual(g2.return_number_of_paths(), 3509)


if __name__ == '__main__':
    unittest.main()