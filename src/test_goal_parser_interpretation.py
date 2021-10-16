import unittest
from answer.easy.goal_parser_interpretation import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.command = [
            'G()(al)',
            'G()()()()(al)',
            '(al)G(al)()()G',
        ]
        self.answers = [
            'Goal',
            'Gooooal',
            'alGalooG',
        ]

    def solution(self, i):
        s = Solution()
        result = s.interpret(self.command[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution1(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
