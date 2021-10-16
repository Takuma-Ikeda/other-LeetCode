import unittest
from answer.easy.sum_of_all_odd_length_subarrays import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 4, 2, 5, 3],
            [1, 2],
            [10, 11, 12],
        ]
        self.answers = [
            58,
            3,
            66,
        ]

    def solution(self, i):
        s = Solution()
        result = s.sumOddLengthSubarrays(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
