import unittest
from answer.easy.reverse_prefix_of_word import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.word = [
            'abcdefd',
            'xyxzxe',
            'abcd',
        ]
        self.ch = [
            'd',
            'z',
            'z',
        ]
        self.answers = [
            'dcbaefd',
            'zxyxxe',
            'abcd',
        ]

    def solution(self, i):
        s = Solution()
        result = s.reversePrefix(self.word[i], self.ch[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
