import unittest
from answer import running_sum_of_1d_array


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 2, 3, 4],
            [1, 1, 1, 1, 1],
            [3, 1, 2, 10, 1]
        ]
        self.answers = [
            [1, 3, 6, 10],
            [1, 2, 3, 4, 5],
            [3, 4, 6, 16, 17],
        ]

    def solution(self, i):
        s = running_sum_of_1d_array.Solution()
        result = s.runningSum(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
