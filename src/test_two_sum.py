import unittest
from answer.easy.two_sum import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [2, 7, 11, 15],
            [3, 2, 4],
            [3, 3],
        ]
        self.targets = [
            9,
            6,
            6,
        ]
        self.answers = [
            [0, 1],
            [1, 2],
            [0, 1],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.twoSum(self.nums[i], self.targets[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
