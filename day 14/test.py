import unittest
import numpy

from main import format_input, part_1, part_2


class Test(unittest.TestCase):
    def test_format_data_day_4(self):

        sequencer = format_input('test_input.txt')
        self.assertEqual(part_1(sequencer), 1588)
        self.assertEqual(part_2(sequencer), 2188189693529)


if __name__ == '__main__':
    unittest.main()