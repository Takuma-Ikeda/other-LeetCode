import unittest
from answer.maximum_nesting_depth_of_the_parentheses import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            "(1+(2*3)+((8)/4))+1",
            "(1)+((2))+(((3)))",
            "1+(2*3)/(2-1)",
            "1",
        ]
        self.answers = [
            3,
            3,
            1,
            0,
        ]

    def solution(self, i):
        s = Solution()
        result = s.maxDepth(self.s[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
