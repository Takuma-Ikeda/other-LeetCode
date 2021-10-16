import unittest
from answer.cells_with_odd_values_in_a_matrix import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.m = [
            2,
            2,
        ]
        self.n = [
            3,
            2,
        ]
        self.indices = [
            [[0, 1], [1, 1]],
            [[1, 1], [0, 0]],

        ]
        self.answers = [
            6,
            0,
        ]

    def solution(self, i):
        s = Solution()
        result = s.oddCells(self.m[i], self.n[i], self.indices[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
