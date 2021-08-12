import unittest
from answer.find_the_highest_altitude import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.gain = [
            [-5, 1, 5, 0, -7],
            [-4, -3, -2, -1, 4, 3, 2]
        ]
        self.answers = [
            1,
            0,
        ]

    def solution(self, i):
        s = Solution()
        result = s.largestAltitude(self.gain[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
