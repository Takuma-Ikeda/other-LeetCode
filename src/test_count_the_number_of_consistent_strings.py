import unittest
from answer.count_the_number_of_consistent_strings import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.allowed = [
            'ab',
            'abc',
            'cad',
        ]
        self.words = [
            ["ad", "bd", "aaab", "baa", "badab"],
            ["a", "b", "c", "ab", "ac", "bc", "abc"],
            ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],
        ]
        self.answers = [
            2,
            7,
            4,
        ]

    def solution(self, i):
        s = Solution()
        result = s.countConsistentStrings(self.allowed[i], self.words[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
