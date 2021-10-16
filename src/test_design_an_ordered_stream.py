import unittest
from answer.easy.design_an_ordered_stream import OrderedStream


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            [
                ["OrderedStream", "insert", "insert", "insert", "insert", "insert"],
                [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]],
            ]
        ]
        self.answers = [
            [None, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]],
        ]

    def solution(self, i):
        num = 1
        o = OrderedStream(self.input[i][1][0][0])
        for key, value in zip(self.input[i][0], self.input[i][1]):
            if key == 'OrderedStream':
                continue
            else:
                result = o.insert(value[0], value[1])
                self.assertEqual(self.answers[i][num], result)
                num += 1

    def test_solution0(self):
        self.solution(0)


if __name__ == "__main__":
    unittest.main()
