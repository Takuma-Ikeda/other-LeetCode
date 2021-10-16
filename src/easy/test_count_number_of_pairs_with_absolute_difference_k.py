import unittest
from answer.count_number_of_pairs_with_absolute_difference_k import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 2, 2, 1],
            [1, 3],
            [3, 2, 1, 5, 4],
        ]
        self.k = [
            1,
            3,
            2,
        ]
        self.answers = [
            4,
            0,
            3,
        ]

    def solution(self, i):
        s = Solution()
        result = s.countKDifference(self.nums[i], self.k[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
