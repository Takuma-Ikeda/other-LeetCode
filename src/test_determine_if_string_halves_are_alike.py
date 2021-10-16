import unittest
from answer.easy.determine_if_string_halves_are_alike import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            "book",
            "textbook",
            "MerryChristmas",
            "AbCdEfGh"
        ]
        self.answers = [
            True,
            False,
            False,
            True,
        ]

    def solution(self, i):
        s = Solution()
        result = s.halvesAreAlike(self.s[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)

    def test_solution3(self):
        self.solution(3)


if __name__ == "__main__":
    unittest.main()
