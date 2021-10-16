import unittest
from answer.easy.robot_return_to_origin import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.moves = [
            "UD",
            "LL",
            "RRDD",
            "LDRRLRUULR"
        ]
        self.answers = [
            True,
            False,
            False,
            False,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.judgeCircle(self.moves[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
