import unittest
from answer.easy.reverse_words_in_a_string_iii import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            "Let's take LeetCode contest",
            "God Ding",
        ]
        self.answers = [
            "s'teL ekat edoCteeL tsetnoc",
            "doG gniD",
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.reverseWords(self.s[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
