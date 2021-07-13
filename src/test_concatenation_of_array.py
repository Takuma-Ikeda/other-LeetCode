import unittest
from answer.concatenation_of_array import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 2, 1],
            [1, 3, 2, 1],
        ]
        self.answers = [
            [1, 2, 1, 1, 2, 1],
            [1, 3, 2, 1, 1, 3, 2, 1],
        ]

    def solution(self, i):
        s = Solution()
        result = s.getConcatenation(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
