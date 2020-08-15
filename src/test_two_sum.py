import unittest
from answer import two_sum


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = two_sum.Solution()
        self.nums = [2, 7, 11, 15]
        self.target = 9
        self.answer = [0, 1]

    def test_solution1(self):
        result = self.s.twoSum(self.nums, self.target)
        self.assertEqual(self.answer, result)


if __name__ == "__main__":
    unittest.main()
