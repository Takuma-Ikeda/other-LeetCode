import unittest
from answer.count_negative_numbers_in_a_sorted_matrix import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.grid = [
            [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
            [[3, 2], [1, 0]],
            [[1, -1], [-1, -1]],
            [[-1]],
        ]
        self.answers = [
            8,
            0,
            3,
            1,
        ]

    def solution(self, i):
        s = Solution()
        result = s.countNegatives(self.grid[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
