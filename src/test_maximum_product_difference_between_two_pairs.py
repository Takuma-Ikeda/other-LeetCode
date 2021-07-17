import unittest
from answer.maximum_product_difference_between_two_pairs import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [5, 6, 2, 7, 4],
            [4, 2, 5, 9, 7, 4, 8],
        ]
        self.answers = [
            34,
            64
        ]

    def solution(self, i):
        s = Solution()
        result = s.maxProductDifference(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
