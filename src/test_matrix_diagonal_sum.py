import unittest
from answer.matrix_diagonal_sum import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.mat = [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[5]],
        ]
        self.answers = [
            25,
            8,
            5,
        ]

    def solution(self, i):
        s = Solution()
        result = s.diagonalSum(self.mat[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
