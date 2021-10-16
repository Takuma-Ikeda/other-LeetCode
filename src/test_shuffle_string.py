import unittest
from answer.easy.shuffle_string import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.Ss = [
            'codeleet',
            'abc',
            'aiohn',
            'aaiougrt',
            'art'
        ]
        self.indices = [
            [4, 5, 6, 7, 0, 2, 1, 3],
            [0, 1, 2],
            [3, 1, 4, 2, 0],
            [4, 0, 2, 6, 7, 3, 1, 5],
            [1, 0, 2]
        ]
        self.answers = [
            'leetcode',
            'abc',
            'nihao',
            'arigatou',
            'rat'
        ]

    def solution(self, i):
        s = Solution()
        result = s.restoreString(self.Ss[i], self.indices[i])
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
