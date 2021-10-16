import unittest
from answer.easy.richest_customer_wealth import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.accounts = [
            [[1, 2, 3], [3, 2, 1]],
            [[1, 5], [7, 3], [3, 5]],
            [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        ]
        self.answers = [
            6,
            10,
            17
        ]

    def solution(self, i):
        s = Solution()
        result = s.maximumWealth(self.accounts[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()

