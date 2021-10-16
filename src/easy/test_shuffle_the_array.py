import unittest
from answer.shuffle_the_array import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [2, 5, 1, 3, 4, 7],
            [1, 2, 3, 4, 4, 3, 2, 1],
            [1, 1, 2, 2]
        ]
        self.ns = [
            3,
            4,
            2
        ]
        self.answers = [
            [2, 3, 5, 4, 1, 7],
            [1, 4, 2, 3, 3, 2, 4, 1],
            [1, 2, 1, 2]
        ]

    def solution(self, i):
        s = Solution()
        result = s.shuffle(self.nums[i], self.ns[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
