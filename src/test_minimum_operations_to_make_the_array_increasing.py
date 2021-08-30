import unittest
from answer.minimum_operations_to_make_the_array_increasing import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 1, 1],
            [1, 5, 2, 4, 1],
            [8],
        ]
        self.answers = [
            3,
            14,
            0,
        ]

    def solution(self, i):
        s = Solution()
        result = s.minOperations(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_solution1(self):
        self.solution(1)

    def test_solution2(self):
        self.solution(2)


if __name__ == "__main__":
    unittest.main()
