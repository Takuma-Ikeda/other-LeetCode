import unittest
from answer.easy.jewels_and_stones import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.J = [
            "aA",
            "z"
        ]
        self.S = [
            "aAAbbbb",
            "ZZ"
        ]
        self.answers = [
            3,
            0
        ]

    def solution(self, i):
        s = Solution()
        result = s.numJewelsInStones(self.J[i], self.S[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
