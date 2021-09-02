import unittest
from answer.maximum_product_of_two_elements_in_an_array import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [3, 4, 5, 2],
            [1, 5, 4, 5],
            [3, 7],
        ]
        self.answers = [
            12,
            16,
            12,
        ]

    def solution(self, i):
        s = Solution()
        result = s.maxProduct(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
