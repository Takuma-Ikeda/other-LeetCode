import unittest
from answer.easy.count_of_matches_in_tournament import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            7,
            14,
        ]
        self.answers = [
            6,
            13,
        ]

    def solution(self, i):
        s = Solution()
        result = s.numberOfMatches(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
