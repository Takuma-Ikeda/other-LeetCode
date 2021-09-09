import unittest
from answer.check_if_all_characters_have_equal_number_of_occurrences import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            'abacbc',
            'aaabb',
        ]

        self.answers = [
            True,
            False,
        ]

    def solution(self, i):
        s = Solution()
        result = s.areOccurrencesEqual(self.s[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
