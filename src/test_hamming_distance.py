import unittest
from answer.easy.hamming_distance import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.x = [
            1,
            3,
        ]
        self.y = [
            4,
            1,
        ]
        self.answers = [
            2,
            1,
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.hammingDistance(self.x[i], self.y[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
