import unittest
from answer import running_sum_of_1d_array


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = running_sum_of_1d_array.Solution()
        self.nums = [
            [1, 2, 3, 4],
            [1, 1, 1, 1, 1],
            [3, 1, 2, 10, 1]
        ]
        self.answer = [
            [1, 3, 6, 10],
            [1, 2, 3, 4, 5],
            [3, 4, 6, 16, 17],
        ]

    def test_solution1(self):
        result = self.s.runningSum(self.nums[0])
        self.assertEqual(self.answer[0], result)

    def test_solution2(self):
        result = self.s.runningSum(self.nums[1])
        self.assertEqual(self.answer[1], result)

    def test_solution3(self):
        result = self.s.runningSum(self.nums[2])
        self.assertEqual(self.answer[2], result)


if __name__ == "__main__":
    unittest.main()
