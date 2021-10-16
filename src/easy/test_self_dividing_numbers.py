import unittest
from answer.self_dividing_numbers import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.left = [
            1,
            47,
        ]
        self.right = [
            22,
            85,
        ]
        self.answers = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22],
            [48, 55, 66, 77],
        ]

    def solution(self, i):
        s = Solution()
        result = s.selfDividingNumbers(self.left[i], self.right[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
