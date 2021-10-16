import unittest
from answer.xor_operation_in_an_array import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.ns = [
            5,
            4,
            1,
            10
        ]
        self.starts = [
            0,
            3,
            7,
            5
        ]
        self.answers = [
            8,
            8,
            7,
            2
        ]

    def solution(self, i):
        s = Solution()
        result = s.xorOperation(self.ns[i], self.starts[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)

    def test_solution3(self):
        self.solution(3)


if __name__ == "__main__":
    unittest.main()

