import unittest
from answer.check_if_the_sentence_is_pangram import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sentence = [
            'thequickbrownfoxjumpsoverthelazydog',
            'leetcode'
        ]
        self.answers = [
            True,
            False,
        ]

    def solution(self, i):
        s = Solution()
        result = s.checkIfPangram(self.sentence[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
