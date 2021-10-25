import unittest
from answer.maximum_number_of_words_you_can_type import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.text = [
            'hello world',
            'leet code',
            'leet code',
        ]
        self.brokenLetters = [
            'ad',
            'lt',
            'e',
        ]
        self.answers = [
            1,
            1,
            0,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.canBeTypedWords(self.text[i], self.brokenLetters[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
