import unittest
from answer.minimum_subsequence_in_non_increasing_order import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [4, 3, 10, 9, 8],
            [4, 4, 7, 6, 7],
            [6],
        ]
        self.answers = [
            [10, 9],
            [7, 7, 6],
            [6],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.minSubsequence(self.nums[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
