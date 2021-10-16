import unittest
from answer.easy.number_of_strings_that_appear_as_substrings_in_word import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.patterns = [
            ["a", "abc", "bc", "d"],
            ["a", "b", "c"],
            ["a", "a", "a"],
        ]
        self.word = [
            "abc",
            "aaaaabbbbb",
            "ab",
        ]
        self.answers = [
            3,
            2,
            3,
        ]

    def solution(self, i):
        s = Solution()
        result = s.numOfStrings(self.patterns[i], self.word[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
