import unittest
from answer.check_if_word_equals_summation_of_two_words import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.firstWord = [
            'acb',
            'aaa',
            'aaa',
        ]
        self.secondWord = [
            'cba',
            'a',
            'a',
        ]
        self.targetWord = [
            'cdb',
            'aab',
            'aaaa',
        ]
        self.answers = [
            True,
            False,
            True,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.isSumEqual(self.firstWord[i], self.secondWord[i], self.targetWord[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
