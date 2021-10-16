import unittest
from answer.easy.build_array_from_permutation import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [0, 2, 1, 5, 3, 4],
            [5, 0, 1, 2, 3, 4],
        ]
        self.answers = [
            [0, 1, 2, 4, 5, 3],
            [4, 5, 0, 1, 2, 3],
        ]

    def solution(self, i):
        s = Solution()
        result = s.buildArray(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
