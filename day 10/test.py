import unittest
import numpy

from main import format_input, check_incorrect_lines, check_incomplete_lines


class TestSum(unittest.TestCase):
    def test_format_data_day_4(self):
        """
        Test the correct formatting of the input data
        """
        formatted_input = format_input('test_input.txt')
        numpy.testing.assert_array_equal(formatted_input, ['[({(<(())[]>[[{[]{<()<>>',
                                                           '[(()[<>])]({[<{<<[]>>(',
                                                           '{([(<{}[<>[]}>{[]{[(<()>',
                                                           '(((({<>}<{<{<>}{[]{[]{}',
                                                           '[[<[([]))<([[{}[[()]]]',
                                                           '[{[{({}]{}}([{[{{{}}([]',
                                                           '{<[[]]>}<{[{[{[]{()[[[]',
                                                           '[<(<(<(<{}))><([]([]()',
                                                           '<{([([[(<>()){}]>(<<{{',
                                                           '<{([{{}}[<[[[<>{}]]]>[]]'])
        self.assertEquals(check_incorrect_lines(formatted_input), 26397)
        self.assertEquals(check_incomplete_lines(formatted_input), 288957)


if __name__ == '__main__':
    unittest.main()