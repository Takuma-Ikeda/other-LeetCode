import unittest
from answer.replace_all_digits_with_characters import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):

        self.s = [
            "a1c1e1",
            "a1b2c3d4e",
        ]
        self.answers = [
            "abcdef",
            "abbdcfdhe"
        ]

    def solution(self, i):
        s = Solution()
        result = s.replaceDigits(self.s[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
