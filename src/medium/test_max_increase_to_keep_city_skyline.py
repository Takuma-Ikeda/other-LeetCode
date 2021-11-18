import unittest
from answer.max_increase_to_keep_city_skyline import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.grid = [
            [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]],
            [[0, 0, 0], [0 ,0 ,0], [0, 0, 0]],
        ]
        self.answers = [
            35,
            0,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.maxIncreaseKeepingSkyline(self.grid[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
