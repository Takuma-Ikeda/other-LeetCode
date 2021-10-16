import unittest
from answer.easy.to_lower_case import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):

        self.s = [
            "Hello",
            "here",
            "LOVELY",
        ]
        self.answers = [
            "hello",
            "here",
            "lovely"
        ]

    def solution(self, i):
        s = Solution()
        result = s.toLowerCase(self.s[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
