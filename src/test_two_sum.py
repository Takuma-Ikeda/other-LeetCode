import unittest
from answer.two_sum import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [2, 7, 11, 15]
        ]
        self.targets = [
            9
        ]
        self.answers = [
            [0, 1]
        ]

    def solution(self, i):
        s = Solution()
        result = s.twoSum(self.nums[i], self.targets[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        self.solution(0)


if __name__ == "__main__":
    unittest.main()
