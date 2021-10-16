import unittest
from answer.increasing_decreasing_string import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            'aaaabbbbcccc',
            'rat',
            'leetcode',
            'ggggggg',
            'spo'

        ]
        self.answers = [
            'abccbaabccba',
            'art',
            'cdelotee',
            'ggggggg',
            'ops',
        ]

    def solution(self, i):
        s = Solution()
        result = s.sortString(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)

    def test_solution3(self):
        self.solution(3)

    def test_solution4(self):
        self.solution(4)


if __name__ == "__main__":
    unittest.main()
