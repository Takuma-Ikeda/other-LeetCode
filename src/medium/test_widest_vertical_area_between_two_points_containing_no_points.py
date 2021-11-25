import unittest
from answer.widest_vertical_area_between_two_points_containing_no_points import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.points = [
            [[8, 7], [9, 9], [7, 4], [9, 7]],
            [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
        ]
        self.answers = [
            1,
            3,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.maxWidthOfVerticalArea(self.points[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
