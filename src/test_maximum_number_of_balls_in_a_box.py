import unittest
from answer.easy.maximum_number_of_balls_in_a_box import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.lowLimit = [
            1,
            5,
            19,
        ]
        self.highLimit = [
            10,
            15,
            28,
        ]
        self.answers = [
            2,
            2,
            2,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.countBalls(self.lowLimit[i], self.highLimit[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
