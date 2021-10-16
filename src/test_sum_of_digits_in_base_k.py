import unittest
from answer.easy.sum_of_digits_in_base_k import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.n = [
            34,
            10,
        ]
        self.k = [
            6,
            10,
        ]
        self.answers = [
            9,
            1,
        ]

    def solution(self, i):
        s = Solution()
        result = s.sumBase(self.n[i], self.k[i])
        self.assertEqual(self.answers[i], result)

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            self.solution(i)


if __name__ == "__main__":
    unittest.main()
