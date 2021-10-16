import unittest
from answer.easy.number_of_good_pairs import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 2, 3, 1, 1, 3],
            [1, 1, 1, 1],
            [1, 2, 3]
        ]
        self.answers = [
            4,
            6,
            0
        ]

    def solution(self, i):
        s = Solution()
        result = s.numIdenticalPairs(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
