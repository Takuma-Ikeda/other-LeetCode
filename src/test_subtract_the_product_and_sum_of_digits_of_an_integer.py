import unittest
from answer.easy.subtract_the_product_and_sum_of_digits_of_an_integer import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.ns = [
            234,
            4421
        ]
        self.answers = [
            15,
            21
        ]

    def solution(self, i):
        s = Solution()
        result = s.subtractProductAndSum(self.ns[i])
        self.assertEqual(self.answers[i], result)

    def test_solution0(self):
        self.solution(0)

    def test_soution1(self):
        self.solution(1)


if __name__ == "__main__":
    unittest.main()
