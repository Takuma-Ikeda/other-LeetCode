import unittest
from answer.sum_of_all_subset_xor_totals import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 3],
            [5, 1, 6],
            [3, 4, 5, 6, 7, 8],
        ]
        self.answers = [
            6,
            28,
            480
        ]

    def solution(self, i):
        s = Solution()
        result = s.subsetXORSum(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
