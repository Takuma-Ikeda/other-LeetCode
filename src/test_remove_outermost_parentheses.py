import unittest
from answer.remove_outermost_parentheses import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):

        self.s = [
            '(()())(())',
            '(()())(())(()(()))',
        ]
        self.answers = [
            '()()()',
            '()()()()(())',
        ]

    def solution(self, i):
        s = Solution()
        result = s.removeOuterParentheses(self.s[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
