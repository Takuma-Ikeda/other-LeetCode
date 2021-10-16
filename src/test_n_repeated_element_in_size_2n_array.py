import unittest
from answer.easy.n_repeated_element_in_size_2n_array import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nums = [
            [1, 2, 3, 3],
            [2, 1, 2, 5, 3, 2],
            [5, 1, 5, 2, 5, 3, 5, 4],
        ]
        self.answers = [
            3,
            2,
            5,
        ]

    def solution(self, i):
        s = Solution()
        result = s.repeatedNTimes(self.nums[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
