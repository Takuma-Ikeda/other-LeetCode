import unittest
from answer.reverse_string import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            ["h", "e", "l", "l", "o"],
            ["H", "a", "n", "n", "a", "h"],
        ]
        self.answers = [
            ["o", "l", "l", "e", "h"],
            ["h", "a", "n", "n", "a", "H"],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            s.reverseString(self.s[i])
            self.assertEqual(self.answers[i], self.s[i])


if __name__ == "__main__":
    unittest.main()
