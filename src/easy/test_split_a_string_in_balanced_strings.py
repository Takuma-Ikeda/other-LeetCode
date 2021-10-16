import unittest
from answer.split_a_string_in_balanced_strings import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = [
            'RLRRLLRLRL',
            'RLLLLRRRLR',
            'LLLLRRRR',
            'RLRRRLLRLL',
        ]
        self.answers = [
            4,
            3,
            1,
            2
        ]

    def solution(self, i):
        s = Solution()
        result = s.balancedStringSplit(self.s[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)

    def test_solution3(self):
        self.solution(3)


if __name__ == "__main__":
    unittest.main()
