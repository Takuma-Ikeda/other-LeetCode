import unittest
from answer.sum_of_unique_elements import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 2, 3, 2],
            [1, 1, 1, 1, 1],
            [1, 2, 3, 4, 5],
        ]
        self.answers = [
            4,
            0,
            15,
        ]

    def solution(self, i):
        s = Solution()
        result = s.sumOfUnique(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
