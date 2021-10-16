import unittest
from answer.unique_morse_code_words import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.words = [
            ["gin", "zen", "gig", "msg"],
            ["a"],
        ]

        self.answers = [
            2,
            1,
        ]

    def solution(self, i):
        s = Solution()
        result = s.uniqueMorseRepresentations(self.words[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
