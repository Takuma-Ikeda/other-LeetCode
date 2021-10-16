import unittest
from answer.easy.create_target_array_in_the_given_order import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [0, 1, 2, 3, 4],
            [1, 2, 3, 4, 0],
            [1],
        ]
        self.indexes = [
            [0, 1, 2, 2, 1],
            [0, 1, 2, 3, 0],
            [0]
        ]
        self.answers = [
            [0, 4, 1, 3, 2],
            [0, 1, 2, 3, 4],
            [1]
        ]

    def solution(self, i):
        s = Solution()
        result = s.createTargetArray(self.nums[i], self.indexes[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
