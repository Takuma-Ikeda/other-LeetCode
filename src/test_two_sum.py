import unittest
from answer import two_sum


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
        s = two_sum.Solution()
        result = s.twoSum(self.nums[i], self.targets[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        self.solution(0)


if __name__ == "__main__":
    unittest.main()
