import unittest
from answer.easy.final_prices_with_a_special_discount_in_a_shop import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.prices = [
            [8, 4, 6, 2, 3],
            [1, 2, 3, 4, 5],
            [10, 1, 1, 6],
        ]
        self.answers = [
            [4, 2, 4, 2, 3],
            [1, 2, 3, 4, 5],
            [9, 0, 1, 6],
        ]

    def test_solution(self):
        for i in range(len(self.answers)):
            print('----- TEST NO.%i START -----' % i)
            s = Solution()
            result = s.finalPrices(self.prices[i])
            self.assertEqual(self.answers[i], result)


if __name__ == "__main__":
    unittest.main()
