import unittest
from answer.merge_strings_alternately import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.word1 = [
            'abc',
            'ab',
            'abcd',
        ]
        self.word2 = [
            'pqr',
            'pqrs',
            'pq',
        ]
        self.answers = [
            'apbqcr',
            'apbqrs',
            'apbqcd',
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.mergeAlternately(self.word1[i], self.word2[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
