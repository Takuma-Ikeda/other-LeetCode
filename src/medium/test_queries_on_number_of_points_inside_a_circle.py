import unittest
from answer.queries_on_number_of_points_inside_a_circle import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.points = [
            [[1, 3], [3, 3], [5, 3], [2, 2]],
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
        ]
        self.queries = [
            [[2, 3, 1], [4, 3, 1], [1, 1, 2]],
            [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]],
        ]
        self.answers = [
            [3, 2, 2],
            [2, 3, 2, 4]
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.countPoints(self.points[i], self.queries[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
