import unittest
from answer.easy.minimum_time_visiting_all_points import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.points = [
            [[1, 1], [3, 4], [-1, 0]],
            [[3, 2], [-2, 2]],
        ]

        self.answers = [
            7,
            5,
        ]

    def solution(self, i):
        s = Solution()
        result = s.minTimeToVisitAllPoints(self.points[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
