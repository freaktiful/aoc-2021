import unittest
import numpy as np

from main import format_input, part_1, part_2


class TestSum(unittest.TestCase):
    def test_enhance(self):
        key, data = format_input('test_input.txt')
        data_part_1 = part_1(data, key)
        self.assertEqual(np.count_nonzero(data_part_1 == '#'), 35)
        data_part_2 = part_2(data, key)
        self.assertEqual(np.count_nonzero(data_part_2 == '#'), 3351)


if __name__ == '__main__':
    unittest.main()