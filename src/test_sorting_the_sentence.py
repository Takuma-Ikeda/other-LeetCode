import unittest
from answer.easy.sorting_the_sentence import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.str = [
            'is2 sentence4 This1 a3',
            'Myself2 Me1 I4 and3',
        ]
        self.answers = [
            'This is a sentence',
            'Me Myself and I',
        ]

    def solution(self, i):
        s = Solution()
        result = s.sortSentence(self.str[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
