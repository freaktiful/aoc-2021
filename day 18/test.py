import unittest

from main import SnailfishNumber, format_input, part_1


class TestSum(unittest.TestCase):
    def test_explode(self):
        a = SnailfishNumber(None, '[[[[9,8],1],2],3]', '4')
        a.explode()
        self.assertEqual(a.print_number(), '[[[[0,9],2],3],4]')

        b = SnailfishNumber(None, '7', '[6,[5,[4,[3,2]]]]')
        b.explode()
        self.assertEqual(b.print_number(), '[7,[6,[5,[7,0]]]]')

        c = SnailfishNumber(None, '[6,[5,[4,[3,2]]]]', '1')
        c.explode()
        self.assertEqual(c.print_number(), '[[6,[5,[7,0]]],3]')

        d = SnailfishNumber(None, '[3,[2,[1,[7,3]]]]', '[6,[5,[4,[3,2]]]]')
        d.explode()
        self.assertEqual(d.print_number(), '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')

        e = SnailfishNumber(None, '[3,[2,[8,0]]]', '[9,[5,[4,[3,2]]]]')
        e.explode()
        self.assertEqual(e.print_number(), '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')

        f = SnailfishNumber(None, '[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]')
        f.reduce()
        self.assertEqual(f.print_number(), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

    def test_reduce(self):
        formatted_input = format_input('test_input_5.txt')
        number, magnitude = part_1(formatted_input)
        self.assertEqual(number.print_number(), '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')
        self.assertEqual(magnitude, 4140)

        formatted_input = format_input('test_input.txt')
        number, magnitude = part_1(formatted_input)
        self.assertEqual(number.print_number(), '[[[[1,1],[2,2]],[3,3]],[4,4]]')
        self.assertEqual(magnitude, 445)

        formatted_input = format_input('test_input_2.txt')
        number, magnitude = part_1(formatted_input)
        self.assertEqual(number.print_number(), '[[[[3,0],[5,3]],[4,4]],[5,5]]')
        self.assertEqual(magnitude, 791)

        formatted_input = format_input('test_input_3.txt')
        number, magnitude = part_1(formatted_input)
        self.assertEqual(number.print_number(), '[[[[5,0],[7,4]],[5,5]],[6,6]]')
        self.assertEqual(magnitude, 1137)

        formatted_input = format_input('test_input_4.txt')
        number, magnitude = part_1(formatted_input)
        self.assertEqual(number.print_number(), '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
        self.assertEqual(magnitude, 3488)


if __name__ == '__main__':
    unittest.main()