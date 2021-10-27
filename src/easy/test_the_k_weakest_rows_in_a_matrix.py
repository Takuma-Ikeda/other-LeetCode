import unittest
from answer.the_k_weakest_rows_in_a_matrix import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.mat = [
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1]
            ],
            [
                [1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0]
            ],
        ]
        self.k = [
            3,
            2,
        ]
        self.answers = [
            [2, 0, 3],
            [0, 2]
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.kWeakestRows(self.mat[i], self.k[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
