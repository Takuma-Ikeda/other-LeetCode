import unittest
from answer.array_partition_i import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 4, 3, 2],
            [6, 2, 6, 5, 1, 2],
        ]
        self.answers = [
            4,
            9,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.arrayPairSum(self.nums[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
